from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from basic_ecommerce.apps.products.models import Product

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('product')
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id

        product_id = request.data['product']
        product = get_object_or_404(Product, pk=product_id)

        request_quantity = request.data['item_quantity']

        if (product.stock < request_quantity):
            return Response({'detail': 'Stock unavailable.'},
                            status=status.HTTP_400_BAD_REQUEST)

        product.stock -= request_quantity
        product.save()

        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        order = self.queryset.get(pk=order_id)
        product = order.product

        request_quantity = request.data['item_quantity']

        quantity_diff = request_quantity - order.item_quantity

        if product.stock < quantity_diff:
            return Response({'detail': 'Stock unavailable.'},
                            status=status.HTTP_400_BAD_REQUEST)

        product.stock -= quantity_diff
        product.save()

        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        order_id = kwargs.get('pk')
        order = self.queryset.get(pk=order_id)
        product = order.product

        product.stock += order.item_quantity
        product.save()

        return super().destroy(request, *args, **kwargs)
