"""This file contains the class Employee page with the methods: create_employee_record,
get_employee, get_all_employee and delete_employee"""

from api.pages.base_page import BasePage
from api.utils.api_methods import ApiMethod
from api.utils.api_body import api_body


class EmployeePage(BasePage):
    """Class representing employee page."""
    def create_employee_record(self):
        """Method returning the response with status OK or with too many requests
         based on url, api method post and api body"""
        url = "https://dummy.restapiexample.com/api/v1/create"
        return self.make_api_request(url, api_method=ApiMethod.POST.value,
                                     api_body=api_body)

    def get_employee(self, employee_id):
        """Method returning the response with status OK or with too many requests
         based on url and api method get"""
        url = f"https://dummy.restapiexample.com/api/v1/employee/{employee_id}"
        return self.make_api_request(url, api_method=ApiMethod.GET.value)

    def get_all_employees(self):
        """Method returning the response with status OK or with too many requests
         based on url and api method get"""
        url = "https://dummy.restapiexample.com/api/v1/employees"
        return self.make_api_request(url, api_method=ApiMethod.GET.value)

    def delete_employee(self, employee_id):
        """Method returning the response with status OK or with too many requests
         based on url and api method delete """
        url = f"https://dummy.restapiexample.com/api/v1/delete/{employee_id}"
        return self.make_api_request(url, api_method=ApiMethod.DELETE.value)
