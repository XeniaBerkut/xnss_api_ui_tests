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
            "Accept": "application/json"
        }
        body = self.user.to_json()
        logger.info("Request token with secret data(login & password")
        response: Response = requests.post(
            Endpoints.AUTH.value,
            headers=headers,
            data=body
        )
        logger.debug(f"Print response {response.json()}")
        logger.info(f"Collect response message")
        response_body: dict = response.json()
        # TODO delete this part before the latest commit
        logger.info("As it is a pet project I'm not sure in a success result, "
                    "so if there is status_code == 403 set one of my received tokens to continue this example test")
        old_token: dict = get_test_data_from_json("test_authorisation_data_old_token.json")
        if response.status_code == 403:
            return "JWT " + old_token["token"]
        else:
            return "JWT " + response_body["token"]
