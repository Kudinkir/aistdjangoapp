# Generated by Django 2.2.4 on 2019-09-11 13:33

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0023_auto_20190911_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='duration',
            field=models.CharField(blank=True, max_length=255, verbose_name='Длительность, 1 час'),
        ),
        migrations.AlterField(
            model_name='videocourses',
            name='about_course',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='about_course'),
        ),
        migrations.AlterField(
            model_name='videocourses',
            name='students_results',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='students_results'),
        ),
    ]
