import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get(path: str, params: dict | None = None) -> requests.Response:
    url = f"{BASE_URL}{path}"
    return requests.get(url, params=params, timeout=10)
