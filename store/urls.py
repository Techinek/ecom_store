from django.urls import path, include
from rest_framework_nested import routers

from .views import CollectionViewSet, ProductViewSet, ReviewViewSet

app_name = 'store'

# Parent router
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('collections', CollectionViewSet, basename='collection')

# Child router
products_router = routers.NestedDefaultRouter(router, 'products',
                                              lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls))
]
