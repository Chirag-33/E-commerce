# Generated by Django 4.2.7 on 2024-08-02 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_product_category_itemstatus'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItemStatus',
            new_name='ItemStatu',
        ),
    ]
