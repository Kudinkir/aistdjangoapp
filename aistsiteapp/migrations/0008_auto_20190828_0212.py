# Generated by Django 2.2.4 on 2019-08-27 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0007_auto_20190819_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_item',
            name='menu_id',
        ),
        migrations.RemoveField(
            model_name='menu_item',
            name='menu_item_id',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Menu_item',
        ),
    ]