# Generated by Django 2.2.4 on 2019-10-28 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0058_auto_20191025_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
        migrations.AlterField(
            model_name='coursesvariants',
            name='price_link',
            field=models.TextField(blank=True, null=True, verbose_name='id товара'),
        ),
        migrations.AlterField(
            model_name='eventsvariants',
            name='price_link',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='id товара'),
        ),
        migrations.AlterField(
            model_name='subscribe',
            name='published_date',
            field=models.DateTimeField(blank=True, verbose_name='Дата регистрации'),
        ),
    ]
