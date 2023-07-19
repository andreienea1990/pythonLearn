import time
from time import sleep

from api.pages.base_page import BasePage
from api.utils.api_methods import ApiMethod

class EmployeePage(BasePage):

    def get_employee(self, employee_id):
        url = f"https://dummy.restapiexample.com/api/v1/employee/{employee_id}"
        return self.make_api_request(url, api_method=ApiMethod.GET.value)

    def get_all_employees(self):
        url = "https://dummy.restapiexample.com/api/v1/employees"
        return self.make_api_request(url, api_method=ApiMethod.GET.value)

    def delete_employee(self, employee_id):
        url = f"https://dummy.restapiexample.com/api/v1/delete/{employee_id}"
        return self.make_api_request(url, api_method=ApiMethod.DELETE.value)

    def update_employee(self, employee_id):
        url = f"https://dummy.restapiexample.com/api/v1/update/{employee_id}"
        return self.make_api_request(url, api_method=ApiMethod.PUT)git a
