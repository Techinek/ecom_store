from decimal import Decimal
from rest_framework import serializers

from .models import Collection, Product


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(required=False)


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = (serializers.SerializerMethodField(
                      method_name='calculate_with_tax'))

    def calculate_with_tax(self, product):
        return product.unit_price * Decimal(1.1)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory',
                  'unit_price', 'price_with_tax', 'collection']

