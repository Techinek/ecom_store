from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
import pytest


@pytest.mark.django_db
class TestCreateCollection:
    def test_anonymous_user_gets_404(self):
        client = APIClient()
        response = client.post(reverse('store:collections-list'),
                               {'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
