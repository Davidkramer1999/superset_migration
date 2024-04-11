import requests


def import_dashboard(base_url, access_token, file_to_import):
    import_url = f"{base_url}/api/v1/dashboard/import"
    import_headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
    }

    import_payload = {
        'overwrite': 'true',
        'passwords':'{}',
        'ssh_tunnel_passwords':'{}',
        'ssh_tunnel_private_keys': '{}',
        'ssh_tunnel_private_key_passwords': '{}'
    }

    with open(file_to_import, 'rb') as f:
        files = {
            'formData': (file_to_import, f, 'application/zip')
        }
        response = requests.post(import_url, headers=import_headers, files=files, data=import_payload, verify=False)
        
    if response.status_code == 200:
        print("Import successful. Response:", response.json())
    else:
        print("Failed to import dashboard. Status code:", response.status_code)

