from django.db import models

from product.models import Product


# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=100)
    stir = models.CharField(max_length=20, unique=True)
    location_x = models.CharField(max_length=20, null=True, blank=True)
    location_y = models.CharField(max_length=20, null=True, blank=True)


class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_shops')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.shop.name} - {self.product.name} - {self.quantity}"

