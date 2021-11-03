import json
import requests
import csv
import sys
import logging
import zuora_const

# ログ出力の設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#環境
ENV = "SBX3"

def main(argv):
    fileName = argv[1]
    reader = _readCsv(fileName)

    access_token = _calloAuthZuoraApi()

    for row in reader:
        start_date = _callRetrieveSubscriptionZuoraApi(access_token, row['subscriptionId'], row['removeRatePlanId'])
        if start_date is None:
            continue

        _callUpdateSubscriptionZuoraApi(access_token, row['subscriptionId'], row['addProductRatePlanId'], row['removeRatePlanId'], start_date)


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

    return res_body["access_token"]

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

    #TODO ネスト回避
    if res_body["success"] == True:
        rate_plans = res_body["ratePlans"]
        for rate_plan in rate_plans:
            if rate_plan["id"] == remove_rate_plan_id:
                plan_id = rate_plan["PlanId__c"]
                rate_plan_charges = rate_plan["ratePlanCharges"]
                for rate_plan_charge in rate_plan_charges:
                    if rate_plan_charge["ProductCode__c"] == plan_id:
                        effective_start_date = rate_plan_charge["effectiveStartDate"]
                        penalty_start_date__c = rate_plan_charge["PenaltyStartDate__c"]
                        if penalty_start_date__c is None:
                            return effective_start_date
                        else:
                            return penalty_start_date__c

    else:
        raise Exception("サブスクリプション取得処理でエラー"+res_body)


def _callUpdateSubscriptionZuoraApi(access_token, subscription_id, add_rate_plan_id, remove_rate_plan_id, start_date):
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
    
    #TODO 固定値を修正（productRatePlanChargeId、ProductCode__c)
    charge_override = {
        "productRatePlanChargeId": "8ad0965d7bcaa195017bcc829485319e",
        "PenaltyStartDate__c": start_date,
        "ProductCode__c": "0034452",
        "triggerEvent": "USD",
        "triggerDate": "2099-12-31"
    }
    charge_overrides = []
    charge_overrides.append(charge_override)

    #TODO 固定値を修正（contractEffectiveDate、PlanId__c）
    childAddObj = {
        "chargeOverrides": charge_overrides,
        "contractEffectiveDate": "2022-01-01",
        "productRatePlanId": add_rate_plan_id,
        "PlanId__c" :"0034452"
    }
    add_plans = []
    add_plans.append(childAddObj)

    #TODO 固定値を修正（contractEffectiveDate）
    childRemoveObj = {
        "contractEffectiveDate": "2022-01-01",
        "ratePlanId": remove_rate_plan_id
    }
    remove_plans = []
    remove_plans.append(childRemoveObj)

    #TODO 固定値を修正（PlanId__c）
    body = {
        "add": add_plans,
        "remove": remove_plans
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
    else:
        raise Exception("環境を指定してください")

    main(sys.argv)

