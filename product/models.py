from django.db import models
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name,ext


def upload_image_path(instance,filename):
    name,ext= get_filename_ext(filename)
    final_name=f"{instance.id}_{instance.ProductName}{ext}"
    return f"product/{final_name}"

# Create your models here.


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=150, verbose_name='عنوان در URL')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    ProductName = models.CharField(max_length=150, null=False, blank=False)
    ProductDescription = models.TextField(max_length=512, null=False, blank=False)
    ProductPrice = models.IntegerField()
    ProductImage = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name="دسته بندی ها")
    active = models.BooleanField(default=False, verbose_name='فعال / غیرفعال')

    def __str__(self):
        return self.ProductName


class Tag(models.Model):
    title = models.CharField(max_length=120, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='عنوان در url')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    products = models.ManyToManyField(Product, blank=True, verbose_name='محصولات')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'برچسب / تگ'
        verbose_name_plural = 'برچسب ها / تگ ها'
