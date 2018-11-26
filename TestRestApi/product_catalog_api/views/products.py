from rest_framework import mixins
from rest_framework import viewsets

from product_catalog_api.serializers import ProductSerializer
from product_catalog_api.models import Product


class ProductViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin):

    serializer_class = ProductSerializer
    queryset = Product.objects.filter(is_new=True)
