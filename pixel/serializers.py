from .models import CatProducts, Product, Ordered
from rest_framework import serializers


class CatProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatProducts
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordered
        fields = '__all__'