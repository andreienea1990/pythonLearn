"""This file contains the class BasePage with the method make_api_requests."""

from time import sleep
from dataclasses import dataclass
from api.utils.status_codes import StatusCode
from api.utils.api_headers import ApiHeaders


@dataclass
class BasePage:
    """Class representing base page."""
    url: str
    api_method: str
    api_body: int = 0
    headers = ApiHeaders.MOZZILA.value
    print(headers)
    max_retries = 5
    retry_delay = 5  # Delay in seconds between retries

    success_http_codes = [StatusCode.STATUS_OK.value,
                          StatusCode.STATUS_CREATED.value,
                          StatusCode.STATUS_OK.value]

    def __init__(self, api_client):
        self.api_client = api_client

    def make_api_request(self, url: str, api_method: str, api_body: int = 0):
        """Method returning the response with status OK or with too many requests"""
        retry_count = 0
        while retry_count < self.max_retries:
            response = self.api_client.request(url, self.headers, api_method, api_body)
            if response.status_code == StatusCode.STATUS_TOO_MANY_REQUESTS.value:
                retry_count += 1
                sleep(self.retry_delay)
            elif response.status_code in self.success_http_codes:
                return response
            else:
                raise ValueError(f"API request failed with status code: {response.status_code}")
        raise ValueError("API request failed after maximum retries")
