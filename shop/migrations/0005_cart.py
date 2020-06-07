# Generated by Django 2.2.4 on 2020-05-24 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('product_image', models.CharField(max_length=100)),
                ('is_ordered', models.BooleanField(default=False)),
                ('product_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
    ]
