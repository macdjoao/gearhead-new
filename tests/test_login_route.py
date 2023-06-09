import requests
import json

url = "http://localhost:5000/api/v1/login"
headers = {'Content-Type': 'application/json'}


def test_login():
    payload = json.dumps({"email": "johndoe@email.com",
                         "password": "johndoe_password"})
    response = (requests.request(
        "POST", url, headers=headers, data=payload)).json()

    assert 'access_token' in response


def test_login_fail():
    payload = json.dumps({"email": "wrong_mail@email.com",
                         "password": "wrong_password"})
    response = requests.request("POST", url, headers=headers, data=payload)

    assert response.text == 'Incorrect email or password.'
