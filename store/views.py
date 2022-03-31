from django.db.models import Count
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_201_CREATED)

    products = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(products,
                                   many=True,
                                   context={'request': request})
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
def product_detail(request, pk):
    if request.method == 'PUT':
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(instance=product,
                                       data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    collections = (Collection.objects.annotate(
                   products_count=Count('products')).all())
    serializer = CollectionSerializer(collections, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(Collection.objects.annotate(
                                   products_count=Count('products')), pk=pk)
    if request.method == 'PUT':
        serializer = CollectionSerializer(instance=collection,
                                          data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        if collection.products.count() > 0:
            return Response({'error': 'Collection with items can not be '
                                      'deleted'})
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = CollectionSerializer(collection)
    return Response(serializer.data)
