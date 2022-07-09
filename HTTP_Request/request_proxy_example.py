import requests
from requests.auth import HTTPProxyAuth

def start_proxy_session():
    ACCOUNT_USERID = "USERID"
    ACCOUNT_PASSWORD = "PASSWORD"

    proxies = {
        "http":"http://proxy.domainname.com:8080",
        "https":"https://proxy.domainname.com:8080"
    }

    auth = HTTPProxyAuth(ACCOUNT_USERID, ACCOUNT_PASSWORD)
    session = requests.Session()
    session.proxies = proxies
    session.auth = auth

    return session

def api_request():
    session = start_proxy_session()
    url = "https://api.url.com/v1/etc"
    API_TOKEN = "TOKEN"

    headers = {
        'Authorization': f'Bearer {API_TOKEN}',
        'Content-Type': 'Application/json'
    }

    r = session.get(url=url, headers=headers, verify=False)
    session.close()

    return r

def main():
    response = api_request()
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    main()