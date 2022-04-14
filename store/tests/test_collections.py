import pytest
from model_bakery import baker
from rest_framework import status
from rest_framework.reverse import reverse

from store.models import Collection


@pytest.fixture
def create_collection(api_client):
    def generate_collection(collection):
        return api_client.post(reverse('store:collections-list'), collection)
    return generate_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_anonymous_user_gets_401(self, create_collection):
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_not_admin_user_gets_403(self, api_client,
                                     create_collection, authenticate):
        authenticate()
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_invalid_data_returns_400(self, api_client,
                                      create_collection, authenticate):
        authenticate(is_staff=True)
        response = create_collection({'title': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_valid_data_returns_200(self, api_client,
                                    create_collection, authenticate):
        authenticate(is_staff=True)
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0


@pytest.mark.django_db
class TestRetrieveCollection:
    def test_existed_collection_returns_200(self, api_client):
        collection = baker.make(Collection)
        response = api_client.get(reverse('store:collections-detail',
                                          args=[collection.id]))
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            'id': collection.id,
            'title': collection.title,
            'products_count': 0
        }
