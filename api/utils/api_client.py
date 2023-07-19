import requests

from api.utils.api_methods import ApiMethod


class APIClient:

    @staticmethod
    def request(url, headers, method):
        if method == ApiMethod.GET:
            response = requests.get(url, headers=headers)
        elif method == ApiMethod.POST:
            response = requests.post(url, headers=headers, data=None)
        elif method == ApiMethod.PUT:
            response = requests.put(url, headers=headers, data=None)
        elif method == ApiMethod.PATCH:
            response = requests.patch(url, headers=headers, data=None)
        elif method == ApiMethod.DELETE:
            response = requests.delete(url, headers=headers)
        # Add more conditions for other HTTP methods if necessary

        return response
