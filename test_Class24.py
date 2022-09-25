# API Automation



import requests


response = requests.get("https://reqres.in/api/users?page=1")
print(response)
print(response.status_code)
print(response.json())
print(response.headers)

# we need requests package to access the api
# how to test with automation framework
# Pytest
import pytest


@pytest.mark.smoke
def test_users():
    response = requests.get("https://reqres.in/api/users?page=1")
    assert response.status_code == 200
    result = response.json()
    assert result['page'] == 1
    assert result['per_page'] == 6
    assert result['total'] == 12
    assert len(result['data']) > 0
    l1 = result['data']
    is_found = False
    for i in l1:
        if i['email'] == 'george.bluth@reqres.in':
            is_found = True
            break

    assert is_found == True


@pytest.mark.smoke
@pytest.mark.regression
def test_users_invalid_api():
    response = requests.get("https://reqres.in/fsdfsdff/users?page=1")
    assert response.status_code == 404
    assert response is not None

# Pytest
# The file name should start with test_
# The test method name should start with test
# Pep8 standards
# how to run all test cases => pytest -v
# how to run particular test cases => pytest -k testmethodname
# how to group test cases => @pytest.mark.groupname
# how to run grouped test cases => pytest -m groupname
