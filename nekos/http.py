import httpx

from .errors import NothingFound


class RequestAPI:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get(self, endpoint: str) -> dict:
        with httpx.Client(http2=True) as client:
            response = client.get(f"{self.base_url}{endpoint}")
            if response.status_code in [404, 500]:
                raise NothingFound("Unable to contact API.")
        return response.json()


http = RequestAPI("https://nekos.life/api/v2")
