import httpx
from .exceptions import SHKeeperError


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    async def _request(self, method, api_key, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = {"X-Shkeeper-Api-Key": api_key, "Content-Type": "application/json"}
        async with httpx.AsyncClient() as client:
            response = await client.request(method, url, json=data, headers=headers,timeout=10)
            if response.status_code != 200:
                raise SHKeeperError(
                    f"API request failed with status {response.status_code}: {response.text}"
                )
            
            return response.json()

    async def get(self, api_key, endpoint):
        return await self._request("GET", api_key, endpoint)

    async def post(
        self,
        api_key,
        endpoint,
        data,
    ):
        return await self._request("POST", api_key, endpoint, data)
