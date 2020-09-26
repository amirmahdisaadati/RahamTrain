from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields='__all__'


class ProductSerializer(serializers.ModelSerializer):

    categories = ProductCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = '__all__'
        #fields = ('ProductName', 'ProductDescription', 'ProductPrice', 'ProductImage', 'categories',  'active', )


class SingleProductSerializer(serializers.ModelSerializer):

    categories = ProductCategorySerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('ProductName', 'ProductDescription', 'ProductPrice', 'ProductImage', 'categories',  'active', )

