import requests

from .errors import NothingFound


class RequestAPI:
    def __init__(self, base_url) -> None:
        self.base_url = base_url
        self._session = requests.Session()

    def get(self, endpoint: str) -> dict:
        response = self._session.get(f"{self.base_url}{endpoint}")
        if response.status_code in [404, 500]:
            raise NothingFound("Unable to contact API.")
        return response.json()


http = RequestAPI("https://nekos.life/api/v2")
