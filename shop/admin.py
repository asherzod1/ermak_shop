from django.contrib import admin

from shop.models import Shop, ShopProduct


# Register your models here.


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'stir', 'location_x', 'location_y',)
    list_display_links = ("name",)


@admin.register(ShopProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('shop', 'product', 'quantity')
    list_display_links = ("shop", "product")