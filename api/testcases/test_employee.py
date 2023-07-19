import pytest
from api.pages.employee_page import EmployeePage
from api.utils.status_codes import StatusCode
from api.utils.status_messages import ResponseMessages


@pytest.fixture
def employee_page(api_client):
    return EmployeePage(api_client)


def test_get_employee(employee_page):
    employee_id = 1
    response = employee_page.get_employee(employee_id)
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_OK
    assert response_json["status"] == ResponseMessages.SUCCESS
    assert isinstance(response_json["data"], dict)
    assert response_json["data"]["id"] == employee_id
    assert response_json["data"]["employee_name"] == "Tiger Nixon"
    # Add more assertions as needed


def test_get_all_employees(employee_page):
    response = employee_page.get_all_employees()
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_OK
    assert response_json["status"] == ResponseMessages.SUCCESS


def test_delete_employee(employee_page):
    employee_id = 2
    response = employee_page.delete_employee(employee_id)
    status_code = response.status_code
    response_json = response.json()
    assert status_code == StatusCode.STATUS_OK
    assert response_json["status"] == ResponseMessages.SUCCESS
    assert response_json["message"] == ResponseMessages.RECORD_DELETED
