# Generated by Django 2.2.4 on 2019-08-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='related_with',
            field=models.CharField(blank=True, choices=[('video', 'video_courses'), ('event', 'events')], max_length=10),
        ),
    ]