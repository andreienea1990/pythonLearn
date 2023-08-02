"""This file contains the conftest"""
import pytest
from api.utils.api_client import APIClient


@pytest.fixture(scope="session")
def api_client():
    """Method returning the client"""
    # Create an instance of the APIClient
    client = APIClient()
    return client
