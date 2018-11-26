import django_filters.rest_framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from product_catalog_api.serializers import ProductSerializer
from product_catalog_api.models import Product


class ProductView(APIView):
    """
    Товары
    """
    serializer_class = ProductSerializer

    def get(self, request, pk):
        try:
            products = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(products, context={'request': request})
        return Response(serializer.data)


class ProductListView(APIView):
    """
    Список товаров
    """
    serializer_class = ProductSerializer
    filterset_fields = ('is_new',)

    def get(self, request):
        search = django_filters.rest_framework.DjangoFilterBackend()
        products = search.filter_queryset(request, Product.objects.all(), self)
        serializer = ProductSerializer(
            products, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data,
                                       context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


