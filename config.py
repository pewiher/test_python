import requests

class APIClientConfig:
    def __init__(self, base_url: str, api_key: str, timeout: int = 10):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.timeout = timeout
        self.headers = {
            'API-KEY': f'{self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    def get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url, headers=self.headers, params=params, timeout=self.timeout)
        response.raise_for_status()
        return response

    def post(self, endpoint: str, data: dict = None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.post(url, headers=self.headers, json=data, timeout=self.timeout)
        response.raise_for_status()
        return response

    def put(self, endpoint: str, data: dict = None):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.put(url, headers=self.headers, json=data, timeout=self.timeout)
        response.raise_for_status()
        return response

    def delete(self, endpoint: str):
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.delete(url, headers=self.headers, timeout=self.timeout)
        response.raise_for_status()
        return response.status_code == 204
