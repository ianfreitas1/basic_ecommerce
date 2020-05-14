from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'item_quantity', 'total_price',
                  'paid', 'product', 'user')

    def get_total_price(self, instance):
        return instance.item_quantity * instance.product.price
