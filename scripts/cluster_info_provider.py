import requests
import json


def get_cluster_id(workspace_base_url, bearer_token, cluster_name):
    cluster_id = ''

    request_headers = {
        'Authorization': 'Bearer % s' % bearer_token,
        'Content-Type': 'application/json'
    }

    workspace_url = '% s/api/2.0/clusters/list' % workspace_base_url

    response = requests.get(workspace_url, headers=request_headers)

    if not response.status_code == 200:
        raise Exception(response.text)
    else:
        processed_json = response.json()

        for clusterInfo in processed_json["clusters"]:
            if clusterInfo["cluster_name"] == cluster_name:
                cluster_id = clusterInfo["cluster_id"]
                break

    if not cluster_id:
        raise Exception("Unable to find Cluster Information ...")

    return cluster_id
