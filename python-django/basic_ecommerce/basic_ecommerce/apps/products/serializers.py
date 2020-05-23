from rest_framework import serializers
from rest_framework_extensions.serializers import PartialUpdateSerializerMixin
from .models import Product


class ProductSerializer(PartialUpdateSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock')
