import pytest
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse

User = get_user_model()


@pytest.fixture
def create_collection(api_client):
    def generate_collection(collection):
        return api_client.post(reverse('store:collections-list'), collection)
    return generate_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_anonymous_user_gets_401(self, api_client, create_collection):
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_not_admin_user_gets_403(self, api_client, create_collection):
        api_client.force_authenticate(user={})
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_invalid_data_returns_400(self, api_client, create_collection):
        api_client.force_authenticate(user=User(is_staff=True))
        response = create_collection({'title': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_valid_data_returns_200(self, api_client, create_collection):
        api_client.force_authenticate(user=User(is_staff=True))
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0
