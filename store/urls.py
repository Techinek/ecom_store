from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import CollectionViewSet, ProductViewSet

app_name = 'store'

router = SimpleRouter()
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet, basename='collections')

urlpatterns = [
    path('', include(router.urls))
]
