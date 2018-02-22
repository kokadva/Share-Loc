import json
from urllib.parse import urljoin

import requests

workspaces_resource = "workspaces"


class GeoserverShell(object):
    default_headers = {'content-type': 'application/json'}
    url = ""
    credential = None

    def __init__(self, url, username='admin', password='geoserver'):
        self.url = url
        self.credential = (username, password)

    def create_workspace(self, name):
        payload = {'workspace': {'name': name}}
        request_url = urljoin(self.url, workspaces_resource)
        r = requests.post(request_url, data=json.dumps(payload), headers=self.default_headers, auth=self.credential)
        return r.status_code

    def create_store(self, workspace, store, host, port, database, user, password, dbtype):
        resourse = 'workspaces/{workspace}/datastores'.format(workspace=workspace)
        payload = {
            "dataStore": {
                "name": store,
                "connectionParameters": {
                    "entry": [
                        {"@key": "host", "$": host},
                        {"@key": "port", "$": port},
                        {"@key": "database", "$": database},
                        {"@key": "user", "$": user},
                        {"@key": "passwd", "$": password},
                        {"@key": "dbtype", "$": dbtype}
                    ]
                }
            }
        }
        request_url = urljoin(self.url, resourse)
        r = requests.post(request_url, data=json.dumps(payload), headers=self.default_headers, auth=self.credential)
        return r.status_code, r.text

    def get_workspaces(self):
        request_url = urljoin(self.url, workspaces_resource)
        r = requests.get(request_url, headers=self.default_headers, auth=self.credential)
        return r.text

    def publish_layer(self, workspace, store, layer):
        resourse = 'workspaces/{workspace}/datastores/{store}/featuretypes'.format(
            store=store, workspace=workspace)
        payload = {
            "featureType": {
                "name": layer,
            }
        }
        request_url = urljoin(self.url, resourse)
        r = requests.post(request_url, data=json.dumps(payload), headers=self.default_headers, auth=self.credential)
        return r.status_code, r.text
