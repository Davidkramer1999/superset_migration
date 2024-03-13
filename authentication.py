import requests

def authenticate(base_url, username, password, provider):
    payload = {'username': username, 'password': password, 'provider': provider, 'refresh': 'true'}
    # WARNING: setting verify=False disables SSL certificate verification.
    response = requests.post(f"{base_url}/api/v1/security/login", json=payload, verify=False)
    return response.json()


def authenticate_prod(base_url, username, password, provider):    
    with requests.Session() as session:
        login_payload = {
            'username': username,
            'password': password,
            'provider': provider,
            'refresh': 'true'
        }
        login_response = session.post(f"{base_url}/api/v1/security/login", json=login_payload, verify=False)
        
        if login_response.status_code == 200:
            access_token = login_response.json().get("access_token")
            return access_token
        else:
            print(f"Login failed, status code: {login_response.status_code}")
            return None


