# Generated by Django 2.2.4 on 2019-09-13 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0039_auto_20190913_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='videocourses',
            name='lesson_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Кол-во уроков и часов'),
        ),
    ]
