import logging
import sys

import pytest
import requests
from requests.models import Response

from helpers.test_data_helpers import get_test_data_from_json


logger = logging.getLogger()
handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def get_token() -> str:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    body = get_test_data_from_json("secrets.json")
    response: Response = requests.post(
        "https://my.exnessaffiliates.com/api/v2/auth/",
        headers=headers,
        data=body
    )
    if response.status_code == 403:
        return "JWT eyJhbGciOiJSUzI1NiIsImtpZCI6InVzZXIiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiIwYzVmZTBlNWVkMTE0NTE5YmEzNTU1Y2QxNjYzZGExMSIsImV4cCI6MTY5MjM4NTQ4MiwiaXNzIjoiQXV0aGVudGljYXRpb24iLCJpYXQiOjE2OTIzNjM4ODIsInN1YiI6ImZkZDNiZTk4MDUwZTRhZDE5ZTExMDk3MmFjZWNlMzM2IiwiYXVkIjpbInBhcnRuZXJzaGlwIl0sImFkZGl0aW9uYWxfcGFyYW1zIjp7IndsX2lkIjoiODcxMWI4YWEtY2M2OC00MTNhLTgwMzQtYzI3MTZhMmNlMTRhIn19.uvAvuKBljop78PtyL_ZnVU5PovCQKNcx0KzEArkzBKc4DUAcQDBE6XyymJP5Abe2MXl9kBbxEeakq-IG44_trM0Hjczne38Ud5ypq1c_n50CLLY8a-2WD3iVoGud4goChrSx8ZZn-P9fYI5HrBBcCrEw4nsIiL_H-efus3Wfn9dSq1VJxysPzL0yck6qbA4BJ5Q_1ukhQKFc6_SBKDCibOLxVZ4OdLVsJ54mGPcfF2jD06x64GWXt16ZpXjwaA4R4dgU6sP9oeHLNx1zFLWU9IW0Obuz_WGQz3v78_Ph5blKqMZbG2wFxQAa_qB8UnSy64Cel_7jZ0Iy3cnlnFGJ87mBOGdNLP-pMN3D5uEaHi7hp2ie_KdV6u8Ov1Yz7evayMRIsuUPP30yNLylhtNH9jn_k5w4JCc25oDzvzJx4Bf8noYxtZJLQaxYJ9gV_BMsEYWI8wzhj7EwkoyExfygun3WYZwgvv8Vck_VAkaMufXAnI2MmkTQLSdIwjw_tW7uPs5YixOYD_nXBrWLWHa2E9UEyEJKBTuH2_WmAq5BCUg0bfPfRFPQjQGMTprtLnisIB3p3KqM362CUOdkGEHPJYHMhYZ4GGwGmROPACa5vx4GjUq2C1Yg7brMzodJEcmTpj7nHobKTdXwg5xP9w3MNNdypmPv-zk0_HcSp1Bb0jM"
    else:
        return "JWT" + response.content["token"]


@pytest.mark.order(1)
def test_token_validation_failed():
    logging.info("Set header")
    headers = {
        "Accept": "application/json",
        "Authorization": get_token()
    }
    logging.info("Get auth request")
    response = requests.get(
        "https://my.exnessaffiliates.com/api/v2/auth/token/",
        headers=headers)
    logging.info("Check if status_code is correct")
    assert response.status_code == 403, \
        f'Expected status code 403, but was {response.status_code}'


data_partner_status: dict = get_test_data_from_json("test_authorisation_data.json")


@pytest.mark.order(1)
@pytest.mark.parametrize("test_case",
                         data_partner_status,
                         ids=[data["test_case_title"] for data in data_partner_status])
def test_partner_summary(test_case: dict):
    logging.info("Set header and body")
    headers = {
        "Accept": "application/json",
        "Authorization": test_case["data"]["token"]
    }
    logging.info("Get partner summary request")
    response = requests.get(
        "https://my.exnessaffiliates.com/api/v3/partner/summary/",
        headers=headers)
    logging.info("Check if status_code is correct")
    assert response.status_code == test_case["expected_response"], \
        f'Expected {test_case["expected_response"]}, but was {response.status_code}'
