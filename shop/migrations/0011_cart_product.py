# Generated by Django 2.2.4 on 2020-05-27 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20200527_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=150)),
                ('product_price', models.IntegerField(default=0)),
                ('out_of_stock', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=100)),
                ('product_image', models.CharField(max_length=100)),
                ('supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('product_image', models.CharField(max_length=100)),
                ('is_ordered', models.BooleanField(default=False)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
    ]
