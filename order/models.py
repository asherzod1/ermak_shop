from django.db import models
from django.db.models import Sum

from product.models import Product
from users.models import Driver, User


# Create your models here.


class Order(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='orders')
    location_x = models.CharField(max_length=20, null=True, blank=True)
    location_y = models.CharField(max_length=20, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        total_price = self.items.aggregate(Sum('price'))['price__sum']
        self.price = total_price or 0.0
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'client: {self.client}, driver: {self.driver}, price: {self.price}'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'order: {self.order} product: {self.product.name} quantity: {self.quantity}'
