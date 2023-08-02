"""This file contains the class Api Method"""
from enum import Enum


class ApiMethod(Enum):
    """Class representing Api Method"""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"
