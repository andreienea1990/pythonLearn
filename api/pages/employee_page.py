import time
from time import sleep

from api.pages.base_page import BasePage


class EmployeePage(BasePage):

    def get_employee(self, employee_id):
        url = f"https://dummy.restapiexample.com/api/v1/employee/{employee_id}"
        return self.make_api_request(url)

    def get_all_employees(self):
        url = "https://dummy.restapiexample.com/api/v1/employees"
        return self.make_api_request(url)
