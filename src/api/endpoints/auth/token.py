import json
import requests

from api.entities.user import User
from api.enums.endpoints import Endpoints
from requests import Response
from helpers.test_data_helpers import get_test_data_from_json

from src.helpers.logger import Logger

logger = Logger(logging_level='INFO')


class Token:
    def __init__(self, user: User):
        super().__init__()
        self.user = user

    def get_token(self) -> str:
        logger.info("Prepare request to get token")
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookies": "incap_ses_1092_1690367=B/NtIHXo/F7W6xZUMpEnD+u/5GQAAAAAtVIPSSkapkY4CoG0WfJ4gQ==; nlbi_1690367=hRoyAWHl70tds+s4tySDeQAAAAAlHWsUBdMFzsoCshx4GuKh; visid_incap_1690367=8s+FBsQ+SoiTdEMcx3RWX+u/5GQAAAAAQUIPAAAAAADiCTzehVFbE+BUeX5q6k+w",
            "Connection": "keep-alive",
            "User-Agent": "PostmanRuntime/7.32.3"
        }
        body = self.user.to_json()
        logger.info("Request token with secret data(login & password")
        response: Response = requests.post(
            Endpoints.AUTH.value,
            headers=headers,
            data=body
        )
        logger.info(f"Print response {response.json()}")
        assert response.status_code == 200, f'Expected status code 200, but was {response.status_code}'
        logger.info(f"Collect response message")
        response_body: dict = response.json()
        # TODO delete this part before the latest commit
        logger.info("Return token")
        return "JWT " + response_body["token"]
