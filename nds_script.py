from do_calc import do_calc
import json
import argparse

parser = argparse.ArgumentParser(
    prog='NDS Cleanup Helper Script',
    description='Returns list of container sizes, empty containers, and invalid container names',
    epilog='Text under help'
)
parser.add_argument('filename')
parser.add_argument('-t', '--token',help='SAS token')
parser.add_argument('-u','--url',help='Storage Account URL. Ex: "https://<storage account>.blob.core.windows.net/"')

args = parser.parse_args()

token_credential = args.token

with open(args.filename) as file:
    container_list = file.read().splitlines()

result = do_calc(token_credential=token_credential,account_url=args.url,container_list=container_list)
#print (json.loads(result))