# Generated by Django 2.1.3 on 2018-11-20 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_details',
            old_name='produtID',
            new_name='AMT_TOTAL',
        ),
        migrations.RemoveField(
            model_name='product_details',
            name='Category',
        ),
        migrations.AddField(
            model_name='product_details',
            name='CDIESEL',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='MISC',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='OIL',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='RDIESEL',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='SUPER',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='TAX',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='volCDIESEL',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='volPlus',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='volRDIESEL',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='volSUPER',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_details',
            name='volUNLD',
            field=models.IntegerField(null=True),
        ),
    ]
