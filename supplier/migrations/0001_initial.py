# Generated by Django 3.0.2 on 2020-05-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('number', models.CharField(max_length=15)),
                ('pincode', models.PositiveIntegerField()),
                ('GST_number', models.PositiveIntegerField(max_length=30)),
                ('Bank_Account_Details', models.TextField()),
                ('store_name', models.CharField(max_length=50)),
                ('store_description', models.CharField(max_length=200)),
                ('store_address', models.TextField()),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=400)),
                ('sku_of_product', models.PositiveIntegerField(max_length=30)),
                ('price_of_product', models.PositiveIntegerField(max_length=40)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
