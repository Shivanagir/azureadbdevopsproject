import requests

TOKEN_REQUEST_HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

ADB_DATABRICKS_RESOURCE_ID = '2ff814a6-3304-4ab8-85cb-cd0e6f879c1d'
MANAGEMENT_RESOURCE_ID = 'https://management.core.windows.net/'


def get_user_aad_token(token_base_url, app_client_id, user_name, password):
    USER_AAD_TOKEN_REQ_BODY = {
        'grant_type': 'password',
        'client_id': app_client_id,
        'resource': ADB_DATABRICKS_RESOURCE_ID,
        'username': user_name,
        'password': password
    }

    response = requests.get(token_base_url, headers=TOKEN_REQUEST_HEADERS,
                            data=USER_AAD_TOKEN_REQ_BODY)

    if not response.status_code == 200:
        raise Exception(response.text)

    return response.json()['access_token']


def get_management_token(token_base_url, app_client_id, app_secret):
    MANAGEMENT_TOKEN_REQ_BODY = {
        'grant_type': 'client_credentials',
        'client_id': app_client_id,
        'resource': MANAGEMENT_RESOURCE_ID,
        'client_secret': app_secret
    }

    response = requests.get(
        token_base_url, headers=TOKEN_REQUEST_HEADERS, data=MANAGEMENT_TOKEN_REQ_BODY)

    if not response.status_code == 200:
        raise Exception(response.text)

    return response.json()['access_token']
