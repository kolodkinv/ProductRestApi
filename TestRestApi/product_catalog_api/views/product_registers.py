from rest_framework import mixins
from rest_framework import viewsets

from product_catalog_api.serializers import ProductRegisterSerializer
from product_catalog_api.models import ProductRegister


class ProductRegisterViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):

    serializer_class = ProductRegisterSerializer
    queryset = ProductRegister.objects.all()
