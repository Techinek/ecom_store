from django.urls import path

from .views import (CollectionDetail, CollectionList,
                    ProductDetail, ProductList)

app_name = 'store'

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('collections/', CollectionList.as_view(), name='collection-list'),
    path('collections/<int:pk>/', CollectionDetail.as_view(),
         name='collection-detail')
]
