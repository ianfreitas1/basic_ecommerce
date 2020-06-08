from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_delete, post_save

from .signals import update_product_cache


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0)])
    stock = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        db_table = "products"
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


post_save.connect(update_product_cache, sender=Product)
post_delete.connect(update_product_cache, sender=Product)
