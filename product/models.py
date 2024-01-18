from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


def image_upload_path(instance, filename):
    return f"images/{instance.name}/{filename}"


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to=image_upload_path)

    def __str__(self):
        return self.name
