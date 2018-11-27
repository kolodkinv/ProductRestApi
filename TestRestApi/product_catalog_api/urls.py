from django.conf.urls import url, include
from rest_framework import routers

from product_catalog_api.views.products import ProductViewSet
from product_catalog_api.views.product_registers import ProductRegisterViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, 'product')
router.register(r'product-register', ProductRegisterViewSet, 'productregister')

urlpatterns = [
    url(r'^', include(router.urls)),
]