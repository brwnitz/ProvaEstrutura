# Generated by Django 4.2.3 on 2023-07-07 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_inventory', '0009_alter_product_perishable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sales',
            field=models.IntegerField(default=0),
        ),
    ]