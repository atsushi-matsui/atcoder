import json
import requests
import csv
import sys
import logging
import zuora_const
import datetime

# ログ出力の設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#環境
ENV = "SBX3"

def main(argv):
    fileName = argv[1]
    reader = _readCsv(fileName)

    auth_zuora_api_result = _calloAuthZuoraApi()
    access_token = auth_zuora_api_result["access_token"]

    retrieve_product_rate_plans_zuora_api_result = _callRetrieveProductRatePlansZuoraApi(access_token)
    if retrieve_product_rate_plans_zuora_api_result["success"] == False:
        raise Exception("プラン情報の取得に失敗")
    product_rate_plans = retrieve_product_rate_plans_zuora_api_result["productRatePlans"]

    for row in reader:
        product_rate_plan_info = None
        for product_rate_plan in product_rate_plans:
            if product_rate_plan["id"] == row['addProductRatePlanId']:
                product_rate_plan_info = product_rate_plan
                break

        if product_rate_plan_info is None:
            print("プロダクトプランが見つからない。addProductRatePlanId="+row['addProductRatePlanId'])
        else:
            subscription_rate_plan_info = _callRetrieveSubscriptionZuoraApi(access_token, row['subscriptionId'], row['removeRatePlanId'])
            if subscription_rate_plan_info is None:
                print("サブスクリプションプランが見つからない。")
                continue
            
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
    
    #辞書形式
    file = csv.DictReader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    return file

def _subscriptionPlanChange(access_token, subscription_id, add_rate_plan, remove_rate_plan, add_rate_plan_id, remove_rate_plan_id):
    #有効開始日を取得する
    start_date = None
    if remove_rate_plan["success"] == False:
        print("サブスクの取得に失敗しました。")
        return

    #TODO ネストやベー
    rate_plans = remove_rate_plan["ratePlans"]
    for rate_plan in rate_plans:
        if rate_plan["id"] == remove_rate_plan_id:
            plan_id = rate_plan["PlanId__c"]
            rate_plan_charges = rate_plan["ratePlanCharges"]
            for rate_plan_charge in rate_plan_charges:
                if rate_plan_charge["ProductCode__c"] == plan_id:
                    effective_start_date = rate_plan_charge["effectiveStartDate"]
                    penalty_start_date__c = rate_plan_charge["PenaltyStartDate__c"]
                    if penalty_start_date__c is None:
                        start_date = effective_start_date
                    else:
                        start_date = penalty_start_date__c
    
    if start_date is None:
        print("起算日が見つかりません。")
        return
    
    #プロダクトプランを確認
    if add_rate_plan["status"] != "Active":
        print("当該プランのステータスがActiveでない")
        return
    
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

    todayStr = datetime.date.today().strftime('%Y-%m-%d')

    childAddObj = {
        "chargeOverrides": charge_overrides,
        "contractEffectiveDate": todayStr,
        "productRatePlanId": add_rate_plan_id,
        "PlanId__c" :add_rate_plan["PlanId__c"]
    }
    add_plans = []
    add_plans.append(childAddObj)

    childRemoveObj = {
        "contractEffectiveDate": todayStr,
        "ratePlanId": remove_rate_plan_id
    }
    remove_plans = []
    remove_plans.append(childRemoveObj)

    _callUpdateSubscriptionZuoraApi(access_token, subscription_id, add_plans, remove_plans)


def _calloAuthZuoraApi():
    """
    Create an OAuth token
    https://www.zuora.com/developer/api-reference/#tag/OAuth

    Parameters
    ----------
    なし
    
    Returns
    -------
    アクセストークン
    """ 
    url = FQDN + zuora_const.const.OAUTH_RESOURCE
    
    headers = {
        "content-type": "application/x-www-form-urlencoded",
    }

    body = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    #TODO エラーハンドリング
    response = requests.post(
        url,
        headers=headers,
        data=body
    )

    res_body = json.loads(response.text)

    return res_body

def _callRetrieveProductRatePlansZuoraApi(access_token):
    """
    List all product rate plans of a product
    https://www.zuora.com/developer/api-reference/#operation/GET_ProductRatePlans

    Parameters
    ----------
    access_token:str
        zuoraへのアクセストークン
        
    Returns
    -------
    productRatePlanCharges:dict
        販促プランの情報
    """

    url = FQDN + RETRIEVE_HANSOKU_PRODUCT_RATE_PLANS
    headers = {
        "Authorization": "Bearer "+access_token
    }

    response = requests.get(
        url,
        headers=headers
    )

    res_body = json.loads(response.text)

    return res_body


def _callRetrieveSubscriptionZuoraApi(access_token, subscription_id, remove_rate_plan_id):
    """
    Retrieve a subscription by key
    https://www.zuora.com/developer/api-reference/#operation/GET_SubscriptionsByKey

    Parameters
    ----------
    access_token:str
        zuoraへのアクセストークン
    subscription_id:str
        Subscription number or ID.
    remove_rate_plan_id:str
        ID of a rate plan for this subscription.
    start_date
        課金の有効開始日
        
    Returns
    -------
    res_body:dict
        レスポンス情報
    """

    url = FQDN + zuora_const.const.RETRIEVE_SUBSCRIPTION_RESOURCE + subscription_id
    headers = {
        "Authorization": "Bearer "+access_token
    }

    response = requests.get(
        url,
        headers=headers
    )

    res_body = json.loads(response.text)

    return res_body


def _callUpdateSubscriptionZuoraApi(access_token, subscription_id, add, remove):
    """
    Update a subscription
    https://www.zuora.com/developer/api-reference/#operation/PUT_Subscription

    Parameters
    ----------
    access_token:str
        zuoraへのアクセストークン
    subscription_id:str
        Subscription number or ID.
    add_rate_plan_id:str
        ID of a product rate plan for this subscription
    remove_rate_plan_id:str
        ID of a rate plan for this subscription.
    start_date
        課金の有効開始日
        
    Returns
    -------
    res_body:dict
        レスポンス情報
    """

    url = FQDN + zuora_const.const.UPDATE_SUBSCRIPTION_RESOURCE + subscription_id

    headers = {
        "Authorization": "Bearer "+access_token,
        "content-type": "application/json",
    }

    body = {
        "add": add,
        "remove": remove
    }

    #TODO エラーハンドリング
    response = requests.put(
        url,
        headers=headers,
        json=body
    )

    res_body = json.loads(response.text)

    #TODO 削除すること
    print(res_body)

    return res_body

if __name__ == "__main__":
    if ENV == "SBX3":
        FQDN = zuora_const.const.TEST_FQDN
        CLIENT_ID = zuora_const.const.SBX3_CLIENT_ID
        CLIENT_SECRET = zuora_const.const.SBX3_CLIENT_SECRET
        RETRIEVE_HANSOKU_PRODUCT_RATE_PLANS = zuora_const.const.RETRIEVE_HANSOKU_PRODUCT_RATE_PLANS + zuora_const.const.SBX3_HANSOKU_PRODUCT_ID + "/productRatePlan"
    else:
        raise Exception("環境を指定してください")

    main(sys.argv)

