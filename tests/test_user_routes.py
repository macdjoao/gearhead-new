# from get_token import get_token
from faker import Faker
import requests
import json

fake = Faker()


def get_token():
    url = "http://localhost:5000/api/v1/login"
    headers = {'Content-Type': 'application/json'}
    payload = json.dumps({"email": "johndoe@email.com",
                         "password": "johndoe_password"})
    response = (requests.request(
        "POST", url, headers=headers, data=payload)).json()
    return response['access_token']


def test_post_user():
    email = fake.safe_email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = email
    url = "http://localhost:5000/api/v1/user"
    payload = json.dumps({
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "password": password
    })
    headers = {
        'Authorization': f'Bearer {get_token()}',
        'Content-Type': 'application/json'
    }

    print(headers['Authorization'])

    response = (requests.request(
        "POST", url, headers=headers, data=payload)).json()
    print(response)

    assert response["email"] == email
    assert response["first_name"] == first_name
    assert response["last_name"] == last_name
