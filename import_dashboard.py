import requests
import json


def import_dashboard(base_url, access_token, file_to_import, csrf_token):
    import_url = f"{base_url}/api/v1/dashboard/import"
    import_headers = {
        'Authorization': f'Bearer {access_token}',
        'X-CSRFToken': csrf_token,
        'Accept': 'application/json',
    }

    # Note: In this adjusted version, 'Accept' and 'X-CSRFToken' are not set here as 'Accept' is default and 'X-CSRFToken' might not be needed. Adjust based on actual API requirements.
    
    # Preparing the payload for non-file form fields
    import_payload = {
        'overwrite': 'true',
        'passwords':'{}',
        'ssh_tunnel_passwords':'{}',
        'ssh_tunnel_private_keys': '{}',
        'ssh_tunnel_private_key_passwords': '{}'
    }

    # Preparing the files dictionary with the file to import
    with open(file_to_import, 'rb') as f:
        files = {
            'formData': (file_to_import, f, 'application/zip')
        }
        # Note: We combine files and data into the files parameter as per requests library's handling of multipart/form-data
        response = requests.post(import_url, headers=import_headers, files={**files, **import_payload}, data=import_payload, verify=False)
        
        print(f"Import response: {response}")
        print(f"Response Body: {response.text}")
    
    if response.status_code == 200:
        print("Import successful. Response:", response.json())
    else:
        print("Failed to import dashboard. Status code:", response.status_code)

# Example usage
# import_dashboard('http://your-superset-url.com', 'your-access-token', 'path/to/dashboard_export.zip')


# def import_dashboard(base_url, access_token, file_to_import):
#     import_url = f"{base_url}/api/v1/dashboard/import"
#     import_headers = {'Authorization': f'Bearer {access_token["access_token"]}', 'Accept': 'application/json'}
#     # import_payload = {'passwords': {}, 'overwrite': 'true'}
#     import_payload = {
#         'overwrite': 'true',  # Use string 'true'/'false' for form data
#         'passwords': '{}',
#         'ssh_tunnel_passwords': '{}',
#         'ssh_tunnel_private_keys': '{}',
#         'ssh_tunnel_private_key_passwords': '{}'
#     }
#     # files = {'formData': (file_to_import, open(file_to_import, 'rb'))}
#     files = {'file': (file_to_import, open(file_to_import, 'rb'), 'application/zip')}
    
#     response = requests.post(import_url, headers=import_headers, data=import_payload, files=files)
    
#     if response.status_code == 200:
#         try:
#             import_response = response
#             print("Import successful. Response:")
#             print(import_response)
#         except json.JSONDecodeError as e:
#             print("Error decoding JSON in import response:", e)
#             print("Response content:", response.text)
#     else:
#         print(f"Import failed with status code {response.status_code}")





#######################################################################
# import requests
# import json

# def import_dashboard(base_url, access_token, file_to_import):
#     import_url = f"{base_url}/api/v1/dashboard/import"
#     import_headers = {'Authorization': f'Bearer {access_token["access_token"]}', 'accept': 'application/json'}
#     import_payload = {'passwords': {}, 'overwrite': 'true'}
#     files = {'formData': (file_to_import, open(file_to_import, 'rb'))}
    
#     response = requests.post(import_url, headers=import_headers, data=import_payload, files=files)
    
#     if response.status_code == 200:
#         try:
#             import_response = response.json()
#             print("Import successful. Response:")
#             print(json.dumps(import_response, indent=2))
#         except json.JSONDecodeError as e:
#             print("Error decoding JSON in import response:", e)
#             print("Response content:", response.text)
#     else:
#         print(f"Import failed with status code {response.status_code}")
