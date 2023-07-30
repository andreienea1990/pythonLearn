"""This file contains the class Response messages"""
from enum import Enum


class ResponseMessages(Enum):
    """Class representing the most common response messages"""
    SUCCESS = "success"
    FAILED = "failed"
    RECORD_DELETED = "Successfully! Record has been deleted"
