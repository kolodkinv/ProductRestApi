from django.conf.urls import url
from product_catalog_api.views.products import ProductView, ProductListView
from product_catalog_api.views.product_registers import ProductRegisterView,\
    ProductRegisterListView
from product_catalog_api.views.api_root import api_root


urlpatterns = [
    url(r'^$', api_root, name='api-root'),
    url(r'^products/$', ProductListView.as_view(), name='product-list'),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductView.as_view(),
        name='product-detail'),
    url(r'^product-register/$', ProductRegisterListView.as_view(),
        name='productregister-list'),
    url(r'^product-register/(?P<pk>[0-9]+)/$', ProductRegisterView.as_view(),
        name='productregister-detail')
]