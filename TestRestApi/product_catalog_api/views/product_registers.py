from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from product_catalog_api.serializers import ProductRegisterSerializer
from product_catalog_api.models import ProductRegister


class ProductRegisterView(APIView):
    """
    Товары
    """
    serializer_class = ProductRegisterSerializer

    def get(self, request, pk):
        try:
            products = ProductRegister.objects.get(pk=pk)
        except ProductRegister.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductRegisterSerializer(
            products, context={'request': request})
        return Response(serializer.data)


class ProductRegisterListView(APIView):
    """
    Список товаров
    """
    serializer_class = ProductRegisterSerializer

    def get(self, request):
        products = ProductRegister.objects.all()
        serializer = ProductRegisterSerializer(
            products, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductRegisterSerializer(data=request.data,
                                               context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
