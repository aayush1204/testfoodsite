# Generated by Django 2.2.4 on 2020-06-04 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_refunds'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('society_name', models.CharField(max_length=30)),
                ('society_locality', models.CharField(max_length=30)),
                ('society_address', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_code', models.CharField(max_length=10)),
                ('voucher_value', models.IntegerField(default=1)),
                ('society', models.ManyToManyField(to='shop.Society')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='society',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Society'),
        ),
    ]
