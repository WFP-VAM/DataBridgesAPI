import httpx
import datetime
from typing import Optional, Any, List, Dict
import data_bridges_client
import urllib3
import json


class WfpApiToken:
    BASE_URL = "https://api.wfp.org"

    def __init__(self, api_key: str, api_secret: str):
        """
        Args:
            api_key: API key credential to make API requests
            api_secret: API secrets credential to make API requests
        """
        self.api_key = api_key
        self.api_secret = api_secret

    def refresh(self, scopes: Optional[str] = None):
        """
        Refreshes token to make API requests
        Args:
            scopes: API scopes. The default is None
        """
        if scopes is None:
            scopes = []
        resp = httpx.post(
            f"{self.BASE_URL}/token",
            data={"grant_type": "client_credentials", "scope": " ".join(scopes)},
            auth=(self.api_key, self.api_secret),
        )
        resp.raise_for_status()
        resp_data = resp.json()
        received_scopes = set(resp_data["scope"].split(" "))
        if not set(scopes).issubset(received_scopes):
            raise TokenScopeError(f"Could not acquire requested scopes: {scopes}")
        return resp_data["access_token"]

    def refresh_urllib3(self, scopes: Optional[str] = None):
        """
        Refreshes token to make API requests
        Same function as self.refresh but uses urllib3
        """

        if scopes is None:
            scopes = []
        resp = urllib3.request(
            "POST",
            f"{self.BASE_URL}/token",
            body={"grant_type": "client_credentials", "scope": " ".join(scopes)},
            headers=urllib3.make_headers(basic_auth=f"{self.api_key}:{self.api_secret}"),
        )
        return resp

    def refresh_configuration(self):
        """
        Instantiate new client.Configuration with fresh OAuth2 access token
        """
        configuration = data_bridges_client.Configuration()
        configuration.access_token = self.refresh()
        return configuration
