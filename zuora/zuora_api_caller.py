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
        res_body:dict
            レスポンス情報
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
        res_body:dict
            レスポンス情報
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


    def call_retrieve_subscription_zuora_api(self, access_token, subscription_id):
        """
        Retrieve a subscription by key
        https://www.zuora.com/developer/api-reference/#operation/GET_SubscriptionsByKey

        Parameters
        ----------
        access_token:str
            zuoraへのアクセストークン
        subscription_id:str
            Subscription number or ID.
            
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
        add:dict
            プラン変更前のサブスクリプションプラン情報
        remove:dict
            プラン変更後のサブスクリプションプラン情報
            
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

        return res_body
    
    def call_update_invoices_zuora_api(self, access_token, invoices):
        """
        Update invoices
        https://www.zuora.com/developer/api-reference/#operation/PUT_BatchUpdateInvoices

        Parameters
        ----------
        access_token:str
            zuoraへのアクセストークン
        invoices:str
            Container for invoice update details.
            
        Returns
        -------
        res_body:dict
            レスポンス情報
        """

        url = self.fqdn + zuora_const.const.UPDATE_INVOICES

        headers = {
            "Authorization": "Bearer "+access_token,
            "content-type": "application/json",
        }

        body = {
            "invoices": invoices
        }

        #TODO エラーハンドリング
        response = requests.put(
            url,
            headers=headers,
            json=body
        )

        res_body = json.loads(response.text)

        return res_body
    
    def call_update_payment_zuora_api(self, access_token, paymentsId):
        """
        Update a payment
        https://www.zuora.com/developer/api-reference/#operation/PUT_UpdatePayment

        Parameters
        ----------
        access_token:str
            zuoraへのアクセストークン
        paymentsId:str
            回収のzuoraID
            
        Returns
        -------
        res_body:dict
            レスポンス情報
        """

        url = self.fqdn + zuora_const.const.UPDATE_PAYMENT + paymentsId
        print('url='+url)

        headers = {
            "Authorization": "Bearer "+access_token,
            "content-type": "application/json",
        }

        body = {
            "comment": "new comment"
            }

        #TODO エラーハンドリング
        response = requests.put(
            url,
            headers=headers,
            json=body
        )

        res_body = json.loads(response.text)

        return res_body