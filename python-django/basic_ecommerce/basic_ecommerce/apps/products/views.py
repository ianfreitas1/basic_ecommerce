from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_extensions.cache.decorators import cache_response

from .models import Product
from .serializers import ProductSerializer
from .cache import ProductObjectKeyConstructor, ProductListKeyConstructor


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny(), ]
        return super(ProductViewSet, self).get_permissions()

    @cache_response(key_func=ProductObjectKeyConstructor())
    def retrieve(self, *args, **kwargs):
        return super(ProductViewSet, self).retrieve(*args, **kwargs)

    @cache_response(key_func=ProductListKeyConstructor())
    def list(self, *args, **kwargs):
        return super(ProductViewSet, self).list(*args, **kwargs)
