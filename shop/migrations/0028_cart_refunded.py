# Generated by Django 2.2.4 on 2020-06-03 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_remove_supplier_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='refunded',
            field=models.BooleanField(default=False),
        ),
    ]
