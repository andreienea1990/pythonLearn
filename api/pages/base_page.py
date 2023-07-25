from time import sleep
from api.utils.status_codes import StatusCode
from api.utils.api_headers import ApiHeaders
from api.utils.api_body import ApiBody

class BasePage:
    headers = ApiHeaders.MOZZILA.value
    print(headers)
    max_retries = 5
    retry_delay = 5  # Delay in seconds between retries

    def __init__(self, api_client):
        self.api_client = api_client

    def make_api_request(self, url, api_method, api_body):
        retry_count = 0
        while retry_count < self.max_retries:
            response = self.api_client.request(url, self.headers,api_method, api_body)
            if response.status_code == StatusCode.STATUS_OK.value:
                return response
            elif response.status_code == StatusCode.STATUS_TOO_MANY_REQUESTS.value:
                retry_count += 1
                sleep(self.retry_delay)
            else:
                raise ValueError(f"API request failed with status code: {response.status_code}")
        raise ValueError("API request failed after maximum retries")
