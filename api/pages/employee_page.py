import time
from time import sleep

from api.pages.base_page import BasePage
from api.utils.api_methods import ApiMethod

class EmployeePage(BasePage):
    def create_employee(self):
        url = f"https://dummy.restapiexample.com/api/v1/create"
        return self.make_api_request(url, api_method=ApiMethod.POST)

    def get_employee(self, employee_id):
        url = f"https://dummy.restapiexample.com/api/v1/employee/{employee_id}"
        return self.make_api_request(url, api_method=ApiMethod.GET)

    def get_all_employees(self):
        url = "https://dummy.restapiexample.com/api/v1/employees"
        return self.make_api_request(url, api_method=ApiMethod.GET)

    def delete_employee(self, employee_id):
        url = f"https://dummy.restapiexample.com/api/v1/delete/{employee_id}"
        return self.make_api_request(url, api_method=ApiMethod.DELETE)
