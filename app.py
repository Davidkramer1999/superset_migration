import os
from dotenv import load_dotenv
import authentication
import export_dashboard
import import_dashboard

# Load variables from the .env file
load_dotenv()

# Authenticate for export dev
dev_url = os.getenv("SUP_RESET_URL_DEV")
dev_username = os.getenv("DEV_USERNAME")
dev_password = os.getenv("DEV_PASSWORD")
dev_auth_method = os.getenv("DEV_AUTH_METHOD")

access_token = authentication.authenticate(dev_url, dev_username, dev_password, dev_auth_method)

# id of the dashboard to export
export_dashboard_id = 77
# Export dashboard dev
export_response = export_dashboard.export_dashboard(dev_url, access_token, export_dashboard_id)

if export_response.status_code == 200:
    # Authenticate for import prod
    prod_url = os.getenv("SUP_RESET_URL_PROD")
    prod_username = os.getenv("PROD_USERNAME")
    prod_password = os.getenv("PROD_PASSWORD")
    prod_auth_method = os.getenv("PROD_AUTH_METHOD")

    access_token_production, csrf_token =authentication.authenticate_prod(prod_url, prod_username, prod_password, prod_auth_method)

    print(f"Access Token Production: {access_token_production}")
    print(f"Csrf token Production: {csrf_token}")
    # csrf_token = authenticate_prod(prod_url, prod_username, prod_password,prod_auth_method)
    
    # print(f"CSRF Token: {csrf_token}")

    # Import dashboard prod
    import_dashboard.import_dashboard(prod_url, access_token_production, "dashboard_export.zip", csrf_token)
else:
    print(f"Export failed with status code {export_response.status_code}. Import will not be executed.")
