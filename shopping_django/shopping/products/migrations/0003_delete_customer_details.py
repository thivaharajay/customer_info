# Generated by Django 2.1.3 on 2018-11-20 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_customer_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customer_details',
        ),
    ]
