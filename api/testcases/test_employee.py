import pytest
from api.pages.employee_page import EmployeePage


@pytest.fixture
def employee_page(api_client):
    return EmployeePage(api_client)


def test_get_employee(employee_page):
    employee_id = 1
    response = employee_page.get_employee(employee_id)
    assert response["status"] == "success"
    assert isinstance(response["data"], dict)
    assert response["data"]["id"] == employee_id
    assert response["data"]["employee_name"] == "Tiger Nixon"
    # Add more assertions as needed


def test_get_all_employees(employee_page):
    response = employee_page.get_all_employees()
    print(response)
