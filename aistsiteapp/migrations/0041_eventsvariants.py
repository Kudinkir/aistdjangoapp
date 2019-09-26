# Generated by Django 2.2.4 on 2019-09-26 14:12

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0040_videocourses_lesson_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsVariants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('text', tinymce.models.HTMLField(verbose_name='Text')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('price_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Сыылка на оплату')),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aistsiteapp.Events', verbose_name='Семинар')),
            ],
            options={
                'verbose_name': 'Варианты курса',
            },
        ),
    ]