import csv
import sys
import logging
import zuora_const
import datetime
import zuora_api_caller

# ログ出力の設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#環境
ENV = "SBX3"

def main(argv):
    fileName = argv[1]
    reader = _readCsv(fileName)

    auth_zuora_api_result = zuora_api_caller_class.call_oauth_zuora_api()
    access_token = auth_zuora_api_result["access_token"]

    retrieve_product_rate_plans_zuora_api_result = zuora_api_caller_class.call_retrieve_product_rate_plans_zuora_api(access_token)
    if retrieve_product_rate_plans_zuora_api_result["success"] == False:
        raise Exception("販促プラン情報の取得に失敗。")
    # 販促プランの情報を取得
    product_rate_plans = retrieve_product_rate_plans_zuora_api_result["productRatePlans"]

    for row in reader:
        product_rate_plan_info = None
        for product_rate_plan in product_rate_plans:
            if product_rate_plan["id"] == row['addProductRatePlanId']:
                #変更後の販促プランのzuora Idを設定
                product_rate_plan_info = product_rate_plan
                break

        if product_rate_plan_info is None:
            print("プロダクトプランが見つからない。addProductRatePlanId="+row['addProductRatePlanId'])
            return
        subscription_rate_plan_info = zuora_api_caller_class.call_retrieve_subscription_zuora_api(access_token, row['subscriptionId'])
        if subscription_rate_plan_info is None:
            print("サブスクリプションプランが見つからない。removeRatePlanId="+row['removeRatePlanId'])
            continue
        #プラン変更を実行
        _subscriptionPlanChange(access_token, row['subscriptionId'], product_rate_plan_info, subscription_rate_plan_info,row['addProductRatePlanId'], row['removeRatePlanId'])


def _readCsv(file_name):
    """
    ファイル読み込み

    Parameters
    ----------
    file_name:str
        ファイル名（絶対パスで記述）
    
    Returns
    -------
    file:dict
        ファイルの情報
    """
    csv_file = open(file_name, "r", encoding="utf-8", errors="", newline="" )
    
    file = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    return file

def _subscriptionPlanChange(access_token, subscription_id, add_rate_plan, remove_rate_plan, add_rate_plan_id, remove_rate_plan_id):
    #有効開始日を取得する
    start_date = None
    if remove_rate_plan["success"] == False:
        print("サブスクの取得に失敗しました。subscription_id="+subscription_id)
        return

    #TODO ネストやベー
    rate_plans = remove_rate_plan["ratePlans"]
    for rate_plan in rate_plans:
        if rate_plan["id"] == remove_rate_plan_id:
            plan_id = rate_plan["PlanId__c"]
            rate_plan_charges = rate_plan["ratePlanCharges"]
            for rate_plan_charge in rate_plan_charges:
                #販促プランはプランIDと商品IDが等しい課金だけ違約金が発生するので、当該の課金からサービス開始日を取得する
                if rate_plan_charge["ProductCode__c"] == plan_id:
                    effective_start_date = rate_plan_charge["effectiveStartDate"]
                    penalty_start_date__c = rate_plan_charge["PenaltyStartDate__c"]
                    if penalty_start_date__c is None:
                        start_date = effective_start_date
                    else:
                        start_date = penalty_start_date__c
    
    if start_date is None:
        print("起算日が見つかりません。subscription_id="+subscription_id)
        return
    
    #プロダクトプランを確認
    if add_rate_plan["status"] != "Active":
        print("当該プランのステータスがActiveでない。add_rate_plan="+add_rate_plan["id"])
        return
    
    #追加するプランの課金情報を設定する
    charge_overrides = []
    for add_rate_plan_charge in add_rate_plan["productRatePlanCharges"]:
        if(add_rate_plan_charge["ProductCode__c"] == add_rate_plan["PlanId__c"]):
            charge_override = {
                "productRatePlanChargeId": add_rate_plan_charge["id"],
                "PenaltyStartDate__c": start_date,
                "ProductCode__c": add_rate_plan_charge["ProductCode__c"],
                "triggerEvent": "USD",
                "triggerDate": "2099-12-31"
            }
        else:
            charge_override = {
                "productRatePlanChargeId": add_rate_plan_charge["id"],
                "ProductCode__c": add_rate_plan_charge["ProductCode__c"],
                "triggerEvent": "USD",
                "triggerDate": "2099-12-31"
            }
        charge_overrides.append(charge_override)

    today_str = datetime.date.today().strftime('%Y-%m-%d')

    child_add_obj = {
        "chargeOverrides": charge_overrides,
        "contractEffectiveDate": today_str,
        "productRatePlanId": add_rate_plan_id,
        "PlanId__c" :add_rate_plan["PlanId__c"]
    }
    add_plans = []
    add_plans.append(child_add_obj)

    #削除するプランの情報を設定する
    child_remove_obj = {
        "contractEffectiveDate": today_str,
        "ratePlanId": remove_rate_plan_id
    }
    remove_plans = []
    remove_plans.append(child_remove_obj)

    #サブスクリプションの更新
    call_update_subscription_zuora_api_result = zuora_api_caller_class.call_update_subscription_zuora_api(access_token, subscription_id, add_plans, remove_plans)
    
    if call_update_subscription_zuora_api_result["success"]:
        print(subscription_id+"：成功")
    else:
        print(subscription_id+"：失敗")




if __name__ == "__main__":
    if ENV == "SBX3":
        FQDN = zuora_const.const.TEST_FQDN
        CLIENT_ID = zuora_const.const.SBX3_CLIENT_ID
        CLIENT_SECRET = zuora_const.const.SBX3_CLIENT_SECRET
        RETRIEVE_HANSOKU_PRODUCT_RATE_PLANS = zuora_const.const.RETRIEVE_HANSOKU_PRODUCT_RATE_PLANS + zuora_const.const.SBX3_HANSOKU_PRODUCT_ID + "/productRatePlan"
    else:
        raise Exception("存在する環境を指定してください。ENV="+ENV)

    # zuoraAPI呼び出し用のクラス
    zuora_api_caller_class = zuora_api_caller.ZuoraApiCaller(FQDN, CLIENT_ID, CLIENT_SECRET, RETRIEVE_HANSOKU_PRODUCT_RATE_PLANS)

    main(sys.argv)

