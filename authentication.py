import requests

def authenticate(base_url, username, password, provider):
    payload = {'username': username, 'password': password, 'provider': provider}
    response = requests.post(f"{base_url}/api/v1/security/login", json=payload)
    return response.json()
