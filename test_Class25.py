import pytest
import requests
from Class13 import getnumber
import json


def test_get_particular_user():
    response = requests.get("https://reqres.in/api/users/2")
    assert response.status_code == 200
    result = response.json()
    assert result['data']['id'] == 2
    assert result['data']['email'] == 'janet.weaver@reqres.in'


@pytest.mark.parametrize("userid,email", [(2, "janet.weaver@reqres.in"), (3, "emma.wong@reqres.in")])
def test_get_particular_users(userid, email):
    response = requests.get(f"https://reqres.in/api/users/{userid}")
    assert response.status_code == 200
    result = response.json()
    assert result['data']['id'] == userid
    assert result['data']['email'] == email


# skip and xfail

def add(a, b):
    return a + b


@pytest.mark.skip
def test_add():
    result = add(3, 4)
    assert result == 7


@pytest.mark.xfail
def test_add():
    result = add(3, 4)
    assert result == 8


def test_create_valid_user():
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "name": "chandra",
        "job": "IT"
    })

    response = requests.post("https://reqres.in/api/users", headers=headers, data=payload)
    assert response.status_code == 201
    result = response.json()
    assert result['name'] == "chandra"
    assert result['job'] == "IT"
    assert result['id'] is not None
    assert result['createdAt'] is not None


def test_update_user():
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "name": "chandra",
        "job": "IT"
    })
    response = requests.put("https://reqres.in/api/users/2", headers=headers, data=payload)
    assert response.status_code == 200
    result = response.json()
    assert result['name'] == "chandra"
    assert result['job'] == "IT"
    assert result['updatedAt'] is not None


def test_patch_user():
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "name": "chandra"
    })
    response = requests.patch("https://reqres.in/api/users/2", headers=headers, data=payload)
    assert response.status_code == 200
    result = response.json()
    assert result['name'] == "chandra"
    assert result['updatedAt'] is not None


def test_delete_user():
    headers = {
        'Content-Type': 'application/json'
    }
    payload = json.dumps({
        "name": "chandra"
    })
    response = requests.delete("https://reqres.in/api/users/2", headers=headers, data=payload)
    assert response.status_code == 204




