import requests

def export_dashboard(base_url, access_token, dashboard_id):
    url = f"{base_url}/api/v1/dashboard/export/"
    payload = { 'q': f'!({dashboard_id})' }
    headers_auth = {'Authorization': f'Bearer {access_token["access_token"]}', 'Accept': 'application/zip'}
    response = requests.get(url, params=payload, headers=headers_auth)

    if response.status_code == 200:
        with open('dashboard_export.zip', 'wb') as f:
            f.write(response.content)
        print("Export successful. File saved as dashboard_export.zip")

    return response
