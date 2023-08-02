"""This file contains the static method request"""
from dataclasses import dataclass
import requests
from api.utils.api_methods import ApiMethod


@dataclass
class APIClient:
    """Class representing Api Client"""
    @staticmethod
    def request(url: str, headers: str, method: str, json: str):
        """Method returning the response based on url, headers and body"""
        if method == ApiMethod.GET.value:
            response = requests.get(url, headers=headers, timeout=5)
        elif method == ApiMethod.POST.value:
            response = requests.post(url, headers=headers, data=json, timeout=5)
        elif method == ApiMethod.PUT.value:
            response = requests.put(url, headers=headers, data=None, timeout=5)
        elif method == ApiMethod.PATCH.value:
            response = requests.patch(url, headers=headers, data=None, timeout=5)
        elif method == ApiMethod.DELETE.value:
            response = requests.delete(url, headers=headers, timeout=5)
        # Add more conditions for other HTTP methods if necessary
        return response
