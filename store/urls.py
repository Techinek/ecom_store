from django.urls import include, path
from rest_framework_nested import routers

from .views import (CartItemViewSet, CartViewSet, CollectionViewSet,
                    CustomerViewSet, OrderViewSet, ProductViewSet,
                    ProductImageViewSet, ReviewViewSet)

app_name = 'store'

# Parent router
router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('collections', CollectionViewSet, basename='collections')
router.register('carts', CartViewSet, basename='carts')
router.register('customers', CustomerViewSet, basename='customers')
router.register('orders', OrderViewSet, basename='orders')

# Child routers
products_router = routers.NestedDefaultRouter(router, 'products',
                                              lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')
products_router.register('images', ProductImageViewSet,
                         basename='product-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', CartItemViewSet, basename='cart-items')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(products_router.urls)),
    path('', include(carts_router.urls)),
]
