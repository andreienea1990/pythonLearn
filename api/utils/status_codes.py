"""This file contains the class Status Code"""
from enum import Enum


class StatusCode(Enum):
    """Class representing the most used status codes"""
    STATUS_OK = 200
    STATUS_CREATED = 201
    STATUS_ACCEPTED = 202
    STATUS_NO_CONTENT = 204
    STATUS_BAD_REQUEST = 400
    STATUS_UNAUTHORIZED = 401
    STATUS_FORBIDDEN = 403
    STATUS_NOT_FOUND = 404
    STATUS_CONFLICT = 409
    STATUS_TOO_MANY_REQUESTS = 429
    STATUS_INTERNAL_SERVER_ERROR = 500
