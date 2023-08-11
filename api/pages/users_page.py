"""This file contains the class Users page with the methods: create_user_record,
get_user, get_all_users and delete_user"""

from api.pages.base_page import BasePage
from api.utils.api_methods import ApiMethod
from api.utils.api_body import api_body


class UsersPage(BasePage):
    """Class representing users page."""
    def create_user_record(self):
        """Method returning the response with status OK or with too many requests
         based on url, api method post and api body"""
        url = "https://reqres.in/api/users"
        return self.make_api_request(url, api_method=ApiMethod.POST.value,
                                     api_body=api_body)

    def get_user(self, user_id):
        """Method returning the response with status OK or with too many requests
         based on url and api method get"""
        url = f"https://reqres.in/api/users/{user_id}"
        return self.make_api_request(url, api_method=ApiMethod.GET.value)

    def get_all_users(self):
        """Method returning the response with status OK or with too many requests
         based on url and api method get"""
        url = "https://reqres.in/api/users?page=2"
        return self.make_api_request(url, api_method=ApiMethod.GET.value)

    def delete_user(self, user_id):
        """Method returning the response with status OK or with too many requests
         based on url and api method delete """
        url = f"https://reqres.in/api/users/{user_id}"
        return self.make_api_request(url, api_method=ApiMethod.DELETE.value)
