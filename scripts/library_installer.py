import requests
import json
from cluster_info_provider import get_cluster_id


def install_jar_library(workspace_base_url, bearer_token, cluster_name, library_path):
    try:
        cluster_id = get_cluster_id(
            workspace_base_url, bearer_token, cluster_name)

        request_headers = {
            'Authorization': 'Bearer % s' % bearer_token,
            'Content-Type': 'application/json'
        }

        workspace_url = '% s/api/2.0/libraries/install' % workspace_base_url

        request_body = {
            'cluster_id': cluster_id,
            'libraries': [
                {
                    'jar': library_path
                }
            ]
        }

        response = requests.post(
            workspace_url, headers = request_headers, data=json.dumps(request_body))

        if not response.status_code == 200:
            raise Exception(response.text)

        return True
    except Exception as error:
        raise Exception(str(error))
