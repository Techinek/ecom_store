from django.urls import path

from .views import (collection_detail, collection_list,
                    ProductDetail, ProductList)

app_name = 'store'

urlpatterns = [
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('collections/', collection_list, name='collection-list'),
    path('collections/<int:pk>/', collection_detail, name='collection-detail')
]