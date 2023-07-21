import time
from time import sleep

from api.pages.base_page import BasePage
from api.utils.api_methods import ApiMethod
from api.utils.api_body import api_body_content


class EmployeePage(BasePage):
    def create_employee_record(self):
        url = "https://dummy.restapiexample.com/api/v1/create"
        return self.make_api_request(url, api_method=ApiMethod.POST.value, api_body=api_body_content)

    def get_employee(self, employee_id):
        url = f"https://dummy.restapiexample.com/api/v1/employee/{employee_id}"
        return self.make_api_request(url, api_method=ApiMethod.GET.value)

    def get_all_employees(self):
        url = "https://dummy.restapiexample.com/api/v1/employees"
        return self.make_api_request(url, api_method=ApiMethod.GET.value)

    def delete_employee(self, employee_id):
        url = f"https://dummy.restapiexample.com/api/v1/delete/{employee_id}"
        return self.make_api_request(url, api_method=ApiMethod.DELETE.value)
