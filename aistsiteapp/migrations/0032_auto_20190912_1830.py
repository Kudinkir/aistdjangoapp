# Generated by Django 2.2.4 on 2019-09-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0031_auto_20190912_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='on_main',
            field=models.BooleanField(blank=True, default=False, verbose_name='Выводить на главной'),
        ),
        migrations.AlterField(
            model_name='events',
            name='video',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Место проведения'),
        ),
    ]
