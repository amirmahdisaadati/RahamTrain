from django.contrib import admin

# Register your models here.
from .models import Product
from .models import ProductCategory
from .models import Tag


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'ProductName', 'ProductPrice']

    class Meta:
        model = Product


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name']

    class Meta:
        model = ProductCategory


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(Tag)

