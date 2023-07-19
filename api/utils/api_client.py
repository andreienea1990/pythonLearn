import requests


class APIClient:
    @staticmethod
    def request(url, headers, method):
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=None)
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=None)
        elif method == "PATCH":
            response = requests.patch(url, headers=headers, data=None)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        # Add more conditions for other HTTP methods if necessary

        return response
