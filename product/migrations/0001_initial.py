# Generated by Django 3.1.1 on 2020-09-24 22:18

from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProductName', models.CharField(max_length=150)),
                ('ProductDescription', models.TextField(max_length=512)),
                ('ProductPrice', models.IntegerField()),
                ('ProductImage', models.ImageField(blank=True, null=True, upload_to=product.models.upload_image_path)),
            ],
        ),
    ]