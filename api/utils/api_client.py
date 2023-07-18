import requests


class APIClient:
    def get(self, endpoint, headers=None):
        response = requests.get(endpoint, headers=headers)
        return response
