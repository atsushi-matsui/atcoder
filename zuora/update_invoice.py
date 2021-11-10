from common import file
import sys
import logging
import zuora_const
import datetime
import zuora_api_caller

# ログ出力の設定
logger = logging.getLogger()
logger.setLevel(logging.INFO)

#環境
ENV = "SBX2"

def main(argv):
    #ファイル読み込み
    fileName = argv[1]
    reader = file.read_csv(fileName)

    #認証トークンの発行
    auth_zuora_api_result = zuora_api_caller_class.call_oauth_zuora_api()
    access_token = auth_zuora_api_result["access_token"]
    
    #請求を一括更新
    invoice_ids = []
    for row in reader:
        invoice_ids.append(row["invoiceId"])
        if len(invoice_ids) == 50:
            _update_invoice(access_token, invoice_ids)
            invoice_ids.clear()
        
def _update_invoice(access_token, invoice_ids):
    invoices = []
    for id in invoice_ids:
        invoice = {
            "id": id
        }
        invoices.append(invoice)
        
    response = zuora_api_caller_class.call_update_invoices_zuora_api(access_token, invoices)
    print("response="+str(response))
        
if __name__ == "__main__":
    if ENV == "SBX2":
        FQDN = zuora_const.const.TEST_FQDN
        CLIENT_ID = zuora_const.const.SBX2_CLIENT_ID
        CLIENT_SECRET = zuora_const.const.SBX2_CLIENT_SECRET
    else:
        raise Exception("存在する環境を指定してください。ENV="+ENV)

    # zuoraAPI呼び出し用のクラス
    zuora_api_caller_class = zuora_api_caller.ZuoraApiCaller(FQDN, CLIENT_ID, CLIENT_SECRET, '')

    main(sys.argv)