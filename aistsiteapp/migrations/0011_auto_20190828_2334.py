# Generated by Django 2.2.4 on 2019-08-28 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0010_auto_20190828_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blocks',
            old_name='texh_name',
            new_name='tech_name',
        ),
    ]
