# Generated by Django 2.2.4 on 2020-05-27 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='supplier_name',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
