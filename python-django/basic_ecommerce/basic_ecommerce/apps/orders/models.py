from django.core.validators import MinValueValidator
from django.db import models

from basic_ecommerce.apps.products.models import Product
from basic_ecommerce.apps.users.models import User


class Order(models.Model):
    item_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    paid = models.BooleanField(default=False)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='orders')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
