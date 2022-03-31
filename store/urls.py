from django.urls import path

from .views import collection_detail, product_detail, product_list

app_name = 'store'

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('collections/<int:pk>/', collection_detail, name='collection-detail')
]