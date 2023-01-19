# Generated by Django 4.0.3 on 2023-01-18 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InvoiceModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('product_name', models.CharField(max_length=255)),
                ('product_price', models.CharField(max_length=50)),
            ],
        ),
    ]
