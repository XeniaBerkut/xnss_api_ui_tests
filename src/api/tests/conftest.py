import os
import pytest

from api.endpoints.auth.token import Token
from api.entities.user import User
from helpers.test_data_helpers import get_test_data_from_json

secrets_file_path = os.path.join(os.path.dirname(__file__), "secrets.json")


@pytest.fixture()
def partner_token():
    partner_user = User(**get_test_data_from_json(secrets_file_path))
    token = Token(partner_user)
    return token.get_token()
