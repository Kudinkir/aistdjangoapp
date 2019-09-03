from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.timezone import now

class Page(models.Model):
    name =models.CharField(max_length=255)
    seo_title = models.CharField(max_length=255)
    tech_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Техническое название')
    seo_description = models.CharField(max_length=255)
    seo_keywords = models.CharField(max_length=255)
    published_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255,  blank=True, null=True)

    class Meta:
        verbose_name='Страница'
        verbose_name_plural='Страницы'

    def __str__(self):
        return self.name


class Blocks(models.Model):
    tech_name=models.CharField(max_length=255, blank=True, null=True, verbose_name='Техническое имя')
    name=models.CharField(max_length=255)
    block_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='id Block')
    page_id = models.ForeignKey('Page', on_delete=models.CASCADE, blank=True, null=True, verbose_name='related Page')
    text=models.TextField(blank=True)
    images = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name='Блок'
        verbose_name_plural='Блоки'

    def __str__(self):
        return self.name

class VideoCourses(models.Model):
    name=models.CharField(max_length=255)
    text=models.TextField(blank=True)
    images = models.ImageField(upload_to='images/', blank=True)
    video =  models.CharField(max_length=255,  blank=True, null=True)
    slug = models.CharField(max_length=255,  blank=True, null=True)

    class Meta:
        verbose_name='Видеокурс'
        verbose_name_plural='Видеокурсы'

    def __str__(self):
        return self.name

class Events(models.Model):
    name=models.CharField(max_length=255)
    images = models.ImageField(upload_to='images/', blank=True)
    video =  models.CharField(max_length=255,  blank=True, null=True)
    slug = models.CharField(max_length=255,  blank=True, null=True)
    text=models.TextField(blank=True)
    start_date=models.DateTimeField(blank=True, default=now)

    class Meta:
        verbose_name='Событие'
        verbose_name_plural='События'

    def __str__(self):
        return self.name
