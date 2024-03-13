import requests


# Example usage
# get_csrf_token("http://your-superset-url.com", "your-username", "your-password")

def authenticate(base_url, username, password, provider):
    payload = {'username': username, 'password': password, 'provider': provider, 'refresh': 'true'}
    # WARNING: setting verify=False disables SSL certificate verification.
    response = requests.post(f"{base_url}/api/v1/security/login", json=payload, verify=False)
    return response.json()


def authenticate_prod(base_url, username, password, provider):
    login_url = f"{base_url}/api/v1/security/login"
    csrf_url = f"{base_url}/api/v1/security/csrf_token"
    
    with requests.Session() as session:
        login_payload = {'username': username, 'password': password, 'provider': provider, 'refresh': 'true'}
        login_response = session.post(login_url, json=login_payload, verify=False)
        
        if login_response.status_code == 200:
            # print("Login successful")
            access_token = login_response.json().get("access_token")
            
            auth_headers = {
                'Authorization': f'Bearer {access_token}',
                'Accept': 'application/json'
            }
            
            csrf_response = session.get(csrf_url, headers=auth_headers, verify=False)

            if csrf_response.status_code == 200:
                csrf_token = csrf_response.json().get('result')  # Assuming the JSON response structure contains a csrf_token field
                # print(f"CSRF Token: {csrf_token}")
                return access_token, csrf_token  # Return both tokens as a tuple
            else:
                print(f"Failed to get CSRF token, status code: {csrf_response.status_code}")
                return None, None  # Return None for both values if CSRF token fetch fails
        else:
            print(f"Login failed, status code: {login_response.status_code}")
            return None, None  # Return None for both values if login fails

