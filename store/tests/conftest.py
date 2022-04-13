from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
import pytest

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticate(api_client):
    def authenticate_role_user(is_staff=False):
        return api_client.force_authenticate(user=User(is_staff=is_staff))
    return authenticate_role_user
