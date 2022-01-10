import requests
import json


def provision_kv_secret_scope(user_aad_token, management_token,
                       kv_resource_id, kv_dns, organization_id, adb_resource_id,
                       adb_base_url, scope_name):
    HEADERS = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer % s' % user_aad_token,
        'X-Databricks-Azure-SP-Management-Token': management_token,
        'X-Databricks-Org-Id': organization_id,
        'X-Databricks-Azure-Workspace-Resource-Id': adb_resource_id
    }

    BODY = {
        'scope': scope_name,
        'scope_backend_type': 'AZURE_KEYVAULT',
        'backend_azure_keyvault': {
            'resource_id': kv_resource_id,
            'dns_name': kv_dns
        },
        'initial_manage_principal': 'users'
    }

    ADB_URL = '% sapi/2.0/secrets/scopes/create' % adb_base_url

    print(ADB_URL)

    response = requests.post(ADB_URL, headers=HEADERS, data=json.dumps(BODY))

    if not response.status_code == 200:
        raise Exception(response.text)

    return True
