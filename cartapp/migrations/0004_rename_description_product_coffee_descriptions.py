# Generated by Django 4.1 on 2023-01-20 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartapp', '0003_remove_product_coffee_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_coffee',
            old_name='description',
            new_name='descriptions',
        ),
    ]
