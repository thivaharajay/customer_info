# Generated by Django 2.1.3 on 2018-11-20 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.TextField(null=True)),
                ('customerID', models.IntegerField(null=True)),
                ('Address', models.TextField(null=True)),
            ],
        ),
    ]
