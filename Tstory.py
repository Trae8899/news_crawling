import requests
import get_api

tstory_api = get_api.api("TSTORY")
client_id = tstory_api['ID']
client_key = tstory_api['KEY']
client_code=tstory_api['CODE']
redirect_url = "https://monews.tistory.com/"


def request_code():
    url = f"""https://www.tistory.com/oauth/authorize?\
client_id={client_id}\
&redirect_uri={redirect_url}\
&response_type=code\
&state=someValue"""
    
    print(url)

def get_access_token():
    url = f"""https://www.tistory.com/oauth/access_token?\
client_id={client_id}\
&client_secret={client_key}\
&redirect_uri={redirect_url}\
&code={client_code}\
&grant_type=authorization_code"""

    res=requests.get(url)
    
    if res.status_code==200:
        print(res)
        print(res.text.replace('access_token=',''))
    else:
        print(res)

# request_code()
get_access_token()