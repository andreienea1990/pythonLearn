"""This file contains test employee"""
import pytest
from api.pages.employee_page import EmployeePage
from api.utils.status_codes import StatusCode
from api.utils.status_messages import ResponseMessages


@pytest.fixture(name="employee_page")
def employer_page(api_client):
    """This method returning class Employee Page"""
    return EmployeePage(api_client)


def test_create_a_new_employee_record(employee_page):
    """This method represent test create a new employee record"""
    response = employee_page.create_employee_record()
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_OK.value
    assert response_json["data"]["NAME"] == "test"
    assert response_json["data"]["SALARY"] == "123"
    assert response_json["data"]["AGE"] == "23"
    assert response_json['status'] == ResponseMessages.SUCCESS.value


def test_get_employee(employee_page):
    """This method represent test get employee"""
    employee_id = 1
    response = employee_page.get_employee(employee_id)
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_OK.value
    assert response_json["status"] == ResponseMessages.SUCCESS.value
    assert isinstance(response_json["data"], dict)
    assert response_json["data"]["id"] == employee_id
    assert response_json["data"]["employee_name"] == "Tiger Nixon"
    assert response_json["data"]["employee_salary"] == 320800
    assert response_json["data"]["employee_age"] == 61


def test_get_all_employees(employee_page):
    """This method represent test get all employees"""
    response = employee_page.get_all_employees()
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_OK.value
    assert response_json["status"] == ResponseMessages.SUCCESS.value


def test_delete_employee(employee_page):
    """This method represent test delete employee"""
    employee_id = 2
    response = employee_page.delete_employee(employee_id)
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_OK.value
    assert response_json["status"] == ResponseMessages.SUCCESS.value
    assert response_json["message"] == ResponseMessages.RECORD_DELETED.value
