# Generated by Django 2.2.4 on 2019-09-11 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0027_auto_20190911_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitemblocks',
            name='menu_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aistsiteapp.MenuItemBlocks', verbose_name='Имя'),
        ),
    ]