# Generated by Django 4.2.3 on 2023-07-05 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventory', '0003_alter_product_expire_date_alter_product_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
