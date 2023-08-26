"""This file contains test users"""
import pytest
from api.pages.users_page import UsersPage
from api.utils.status_codes import StatusCode


@pytest.fixture(name="users_page")
def user_page(api_client):
    """This method returning class Users Page"""
    return UsersPage(api_client)


def test_create_a_new_user_record(users_page):
    """This method represent test create a new user record"""
    response = users_page.create_user_record()
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_CREATED.value
    assert response_json["NAME"] == "morpheus"
    assert response_json["JOB"] == "leader"


def test_get_user(users_page):
    """This method represent test get user"""
    user_id = 2
    response = users_page.get_user(user_id)
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_OK.value
    assert isinstance(response_json["data"], dict)
    assert response_json["data"]["id"] == user_id
    assert response_json["data"]["email"] == "janet.weaver@reqres.in"
    assert response_json["data"]["first_name"] == "Janet"
    assert response_json["data"]["last_name"] == "Weaver"
    assert response_json["support"]["text"] == "To keep ReqRes free, contributions " \
                                               "towards server costs are appreciated!"


def test_get_all_users(users_page):
    """This method represent test get all users"""
    response = users_page.get_all_users()
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_OK.value
    assert response_json["data"][0]["email"] == "michael.lawson@reqres.in"


def test_delete_user(users_page):
    """This method represent test delete user"""
    user_id = 2
    response = users_page.delete_user(user_id)
    status_code = response.status_code
    assert status_code == StatusCode.STATUS_NO_CONTENT.value
