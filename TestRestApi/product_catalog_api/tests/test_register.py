import unittest
import pytest

from rest_framework.test import APIRequestFactory

from product_catalog_api.models import ProductRegister, Product
from product_catalog_api.views.product_registers import ProductRegisterListView

pytestmark = pytest.mark.django_db


class TestProductRegisters(unittest.TestCase):

    def setUp(self):
        product = Product.objects.create(
            title='N', is_new=True, SKU='1234567891010')
        ProductRegister.objects.create(
            user_email='mail@mail.ru', count=1, action='A', product=product)

    def test_add(self):
        factory = APIRequestFactory()
        request = factory.post('/api/product-register/',
                               {'user_email': 'NAME@mail.ru',
                                'count': 1,
                                'action': 'A',
                                'product': '1234567891010'})
        ProductRegisterListView.as_view()(request)
        records = ProductRegister.objects.all()
        assert len(records) == 2, 'Корректное добавление записи в реестр'

        request = factory.post('/api/product-register/',
                               {'user_email': 'NAME@mail.ru',
                                'count': 1,
                                'action': 'A',
                                'product': '1234567891014'})
        ProductRegisterListView.as_view()(request)
        products = ProductRegister.objects.all()
        assert len(products) == 2, \
            'Добавление записи с несуществующим товаром в реестр'

        request = factory.post('/api/product-register/',
                               {'user_email': 'NAME@mail.ru',
                                'count': 0,
                                'action': 'A',
                                'product': '1234567891010'})
        ProductRegisterListView.as_view()(request)
        products = ProductRegister.objects.all()
        assert len(products) == 2, \
            'Добавление записи с неправильным количеством товаров'

        request = factory.post('/api/product-register/',
                               {'user_email': 'NAME@mail.ru',
                                'count': 1,
                                'action': 'B',
                                'product': '1234567891010'})
        ProductRegisterListView.as_view()(request)
        products = ProductRegister.objects.all()
        assert len(products) == 2, \
            'Добавление записи с неправильной операцией'

    def test_filter(self):
        factory = APIRequestFactory()
        request = factory.get('/api/product-register')
        result = ProductRegisterListView.as_view()(request)
        assert len(result.data) == 1, 'Получение всех записей в реестре'

