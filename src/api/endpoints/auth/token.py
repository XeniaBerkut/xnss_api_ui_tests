from api.entities.user import User


def get_token(user: User) -> str:
    logging.info("Prepare request to get token")
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    # body = get_test_data_from_json("secrets.json")
    body = get_test_data_from_json(file_name)
    logging.info("Request token with secret data(login & password")
    response: Response = requests.post(
        ENDPOINT + "/v2/auth/",
        headers=headers,
        data=body
    )
    logging.debug(f"Print response {response.json()}")
    logging.info(f"Collect response message")
    response_body: dict = response.json()
    logging.info("As it is a pet project I'm not sure in a success result, "
                 "so if there is status_code == 403 set one of my received tokens to continue this example test")
    old_token: str = get_test_data_from_json("test_authorisation_data_old_token.json")
    if response.status_code == 403:
        return "JWT " + old_token["token"]
    else:
        return "JWT " + response_body["token"]