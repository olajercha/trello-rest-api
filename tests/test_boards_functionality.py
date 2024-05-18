import requests
from credentials import baseURL, key, token

existing_board_id = '6648dde44393e55de5b90801'


# create a new board test
def test_create_new_board_expect_200_returned():
    new_board_url = baseURL + "boards/"
    body = {"key": key, "token": token, "name": "Board Name"}

    response = requests.post(new_board_url, json=body)

    assert response.status_code == 200

    response_data = response.json()
    print(response_data)


# update existing board test
def test_update_a_board_expect_200_returned():
    existing_board_url = baseURL + f'boards/{existing_board_id}'
    body = {"key": key, "token": token, "desc": "This is a new description for an existing board."}

    response = requests.put(existing_board_url, json=body)

    assert response.status_code == 200

    response_data = response.json()
    print(response_data)
