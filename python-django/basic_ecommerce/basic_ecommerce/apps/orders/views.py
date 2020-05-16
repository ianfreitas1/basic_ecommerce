from rest_framework import viewsets

from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.select_related('product')
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id

        return super().create(request, *args, **kwargs)
