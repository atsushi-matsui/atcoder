import json
import requests
import zuora_const

class ZuoraApiCaller:
    FQDN = ""

    def __init__(self, fqdn, client_id, client_secret, retrieve_hansoku_product_rate_plans):
        self.fqdn = fqdn
        self.client_id = client_id
        self.client_secret = client_secret
        self.retrieve_hansoku_product_rate_plans = retrieve_hansoku_product_rate_plans

    def call_oauth_zuora_api(self):
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
        url = self.fqdn + zuora_const.const.OAUTH_RESOURCE
        
        headers = {
            "content-type": "application/x-www-form-urlencoded",
        }

        body = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
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

    def call_retrieve_product_rate_plans_zuora_api(self, access_token):
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

        url = self.fqdn + self.retrieve_hansoku_product_rate_plans
        headers = {
            "Authorization": "Bearer "+access_token
        }

        response = requests.get(
            url,
            headers=headers
        )

        res_body = json.loads(response.text)

        return res_body


    def call_retrieve_subscription_zuora_api(self, access_token, subscription_id, remove_rate_plan_id):
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

        url = self.fqdn + zuora_const.const.RETRIEVE_SUBSCRIPTION_RESOURCE + subscription_id
        headers = {
            "Authorization": "Bearer "+access_token
        }

        response = requests.get(
            url,
            headers=headers
        )

        res_body = json.loads(response.text)

        return res_body


    def call_update_subscription_zuora_api(self, access_token, subscription_id, add, remove):
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

        url = self.fqdn + zuora_const.const.UPDATE_SUBSCRIPTION_RESOURCE + subscription_id

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