import requests
# from config import screenapi,screen_auth
import os
from http.client import HTTPSConnection
import base64

from requests.auth import HTTPBasicAuth
import json


api_path = 'http://localhost:8000/uploadfile/?colindex={}'
class Getdata:
    def __init__(self,api):
        self.api = api

    def upload(self,file,colindex=11):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        # resp = requests.post(self.api, verify=False, auth=HTTPBasicAuth('screenshot', 'sdhfjksaf'), json={'file':file,'colindex':colindex},headers=headers)
        resp = requests.post(self.api, verify=False, auth=HTTPBasicAuth('screenshot', 'sdhfjksaf'), json={'file':file,'colindex':colindex},headers=headers)
        print(resp.status_code,resp.reason)
        print(resp.content)

        return resp.content

api = Getdata(api_path)
file_path = r'C:\\Users\\hx\Desktop\\apitetsting.xlsx'
if os.path.exists(file_path):
# filename = api.upload(file=open(file_path,'r'),colindex=11)
    filename = api.upload(file=file_path,colindex=11)
    print(filename)