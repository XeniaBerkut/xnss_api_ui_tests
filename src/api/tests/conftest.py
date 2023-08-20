from api.endpoints.auth.token import get_token
from api.entities.user import User
from helpers.test_data_helpers import get_test_data_from_json


def partner_token():
    partner_user: User = get_test_data_from_json("secrets.json")
    get_token(partner_user)
