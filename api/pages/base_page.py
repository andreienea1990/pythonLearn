import time
from time import sleep


class BasePage:
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0'}
    max_retries = 3
    retry_delay = 3  # Delay in seconds between retries

    def __init__(self, api_client):
        self.api_client = api_client

    def make_api_request(self, url,api_method):
        retry_count = 0
        while retry_count < self.max_retries:
            response = self.api_client.request(url, self.headers,api_method)
            if response.status_code == 200:
                return response
            elif response.status_code == 429:
                retry_count += 1
                sleep(self.retry_delay)
            else:
                raise ValueError(f"API request failed with status code: {response.status_code}")
        raise ValueError("API request failed after maximum retries")
