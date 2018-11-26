import unittest
import pytest

from rest_framework.test import APIRequestFactory

from product_catalog_api.models import Product
from product_catalog_api.views.products import ProductListView

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
        ProductListView.as_view()(request)
        products = Product.objects.all()
        assert len(products) == 2, 'Корректное добавление товара'

        ProductListView.as_view()(request)
        products = Product.objects.all()
        assert len(products) == 2, 'Товар не добавляется при существующем SKU'

        request = factory.post('/api/products/',
                               {'title': 'NAME',
                                'is_new': True,
                                'SKU': '123456789101'})
        ProductListView.as_view()(request)
        products = Product.objects.all()
        assert len(products) == 2, 'Товар недобавляется при неправильном SKU'

    def test_filter(self):
        factory = APIRequestFactory()
        request = factory.get('/api/products?is_new=True')
        result = ProductListView.as_view()(request)
        assert len(result.data) == 1, 'Фильтрация новых товаров'
        assert result.data[0]['is_new'], 'Правильная фильтрация новинок'

        request = factory.get('/api/products?is_new=False')
        result = ProductListView.as_view()(request)
        assert len(result.data) == 0, 'Фильтрация старых товаров'

        request = factory.get('/api/products')
        result = ProductListView.as_view()(request)
        assert len(result.data) == 1, 'Получение всех товаров'



