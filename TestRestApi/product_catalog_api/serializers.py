from rest_framework import serializers

from product_catalog_api.models import Product, ProductRegister


class ProductSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Product
        fields = ('url', 'title', 'SKU', 'date_creation', 'image', 'is_new')

    def validate(self, data):
        if len(data['SKU']) != Product.SKU_LENGTH:
            raise serializers.ValidationError(
                'Длина SKU не соответсвует стандарту EAN-13')
        if not data['SKU'].isdigit():
            raise serializers.ValidationError(
                'SKU должно содержать только цифры')
        return data


class ProductRegisterSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = ProductRegister
        fields = (
            'url', 'date_operation', 'user_email', 'count', 'action', 'product'
        )

    def validate(self, data):
        if data['count'] < 1:
            raise serializers.ValidationError(
                'Количество товара в операции должно быть больше 0')
        return data
