from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


@api_view(['POST'])
def product_create(request):

    data = request.data

    create_product = Product.objects.create(
        title=data['title'],
        price=data['price'],
    )

    serializer = ProductSerializer(create_product, many=False)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def product_list(request):

    paginator = PageNumberPagination()

    paginator.page_size = 2

    products = Product.objects.all()
    
    result_page = paginator.paginate_queryset(products, request)

    serializer = ProductSerializer(result_page, many=True)
    
    paginated_response = paginator.get_paginated_response(serializer.data)

    return paginated_response