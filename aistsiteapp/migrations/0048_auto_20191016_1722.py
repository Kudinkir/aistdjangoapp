# Generated by Django 2.2.4 on 2019-10-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0047_auto_20191016_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='visible',
            field=models.BooleanField(blank=True, default=False, verbose_name='Видимость'),
        ),
        migrations.AddField(
            model_name='videocourses',
            name='visible',
            field=models.BooleanField(blank=True, default=False, verbose_name='Видимость'),
        ),
    ]
