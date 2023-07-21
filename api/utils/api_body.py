from enum import Enum


class ApiBody(Enum):
    NAME: 'test'
    SALARY: 123
    AGE: 23

    @staticmethod
    def api_body_content(apiclient):
        return ApiBody(apiclient)
