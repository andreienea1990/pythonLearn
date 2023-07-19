import requests


class APIClient:
    @staticmethod
    def request(method, url, headers):
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers,data=None)
        elif method == "PUT":
            response = requests.post(url, headers=headers,data=None)
        elif method == "PATCH":
            response = requests.post(url, headers=headers,data=None)
        elif method == "DELETE":
            response = requests.post(url, headers=headers)
        # Add more conditions for other HTTP methods if necessary

        return response