# Generated by Django 2.2.4 on 2019-09-10 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aistsiteapp', '0018_auto_20190910_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesVariants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('text', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.CharField(max_length=255, verbose_name='Цена')),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aistsiteapp.VideoCourses', verbose_name='Видеокурс')),
            ],
            options={
                'verbose_name': 'Варианты курса',
            },
        ),
    ]
