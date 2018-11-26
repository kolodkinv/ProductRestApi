from django.conf.urls import url, include
from rest_framework import routers
# from product_catalog_api.views.products import ProductView, ProductListView, ProductViewSet
# from product_catalog_api.views.product_registers import ProductRegisterView,\
#     ProductRegisterListView
# from product_catalog_api.views.api_root import api_root
from product_catalog_api.views.products import ProductViewSet
from product_catalog_api.views.product_registers import ProductRegisterViewSet

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, 'product')
router.register(r'product-register', ProductRegisterViewSet, 'productregister')

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^$', api_root, name='api-root'),
    # url(r'^products/$', ProductListView.as_view(), name='product-list'),
    # url(r'^products/(?P<pk>[0-9]+)/$', ProductView.as_view(),
    #     name='product-detail'),
    # url(r'^product-register/$', ProductRegisterListView.as_view(),
    #     name='productregister-list'),
    # url(r'^product-register/(?P<pk>[0-9]+)/$', ProductRegisterView.as_view(),
    #     name='productregister-detail')
]