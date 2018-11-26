import unittest
import pytest

from rest_framework.test import APIRequestFactory

from product_catalog_api.models import Product
from product_catalog_api.views.products import ProductViewSet

pytestmark = pytest.mark.django_db


class TestProducts(unittest.TestCase):

    def setUp(self):
        Product.objects.create(title='N', is_new=True, SKU='1234567891010')

    def test_add(self):
        factory = APIRequestFactory()
        request = factory.post('/api/products/',
                               {'title': 'NAME',
                                'is_new': True,
                                'SKU': '1234567891012'})
        ProductViewSet.as_view({'post': 'create'})(request)
        products = Product.objects.all()
        assert len(products) == 2, 'Корректное добавление товара'

        ProductViewSet.as_view({'post': 'create'})(request)
        products = Product.objects.all()
        assert len(products) == 2, 'Товар не добавляется при существующем SKU'

        request = factory.post('/api/products/',
                               {'title': 'NAME',
                                'is_new': True,
                                'SKU': '123456789101'})
        ProductViewSet.as_view({'post': 'create'})(request)
        products = Product.objects.all()
        assert len(products) == 2, 'Товар недобавляется при неправильном SKU'

    def test_filter(self):
        factory = APIRequestFactory()
        request = factory.get('/api/products')
        result = ProductViewSet.as_view({'get': 'list'})(request)
        assert list(result.data.items())[0][1] == 1, 'Получение всех товаров'



