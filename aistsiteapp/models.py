from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from tinymce import HTMLField


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
    tech_name=models.CharField(max_length=255, blank=True, null=True, unique=True,verbose_name='Техническое имя')
    prior=models.IntegerField(verbose_name='Приоритет', default=100)
    name=models.CharField(max_length=255, unique=True)
    block_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='id Block')
    page_id = models.ForeignKey('Page', on_delete=models.CASCADE, blank=True, null=True, verbose_name='related Page')
    text=HTMLField('Text')
    images = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name='Блок'
        verbose_name_plural='Блоки'

    def __str__(self):
        return self.name

class VideoCourses(models.Model):
    name=models.CharField(max_length=255)
    text=HTMLField('Text')
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
    text=HTMLField('Text')
    start_date=models.DateTimeField(blank=True, default=now)

    class Meta:
        verbose_name='Событие'
        verbose_name_plural='События'

    def __str__(self):
        return self.name

class Callback(models.Model):
    user_name=models.CharField(max_length=255, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=255)
    text=HTMLField('Text')
    personal_agree=models.BooleanField()

    class Meta:
        verbose_name='Обратная связь'

    def __str__(self):
        return self.user_name

class Subscribe(models.Model):
    STATUS = (
       ('1-11', ('1-11 недель')),
       ('12-19', ('12-19 недель')),
       ('20-29', ('20-29 недель')),
       ('30-41', ('30-41 недель')),
       ('После родов', ('После родов'))
    )
    user_name=models.CharField(max_length=255, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=255)
    text=models.TextField(blank=True, verbose_name='Неделя беременности',choices=STATUS)
    personal_agree=models.BooleanField()

    class Meta:
        verbose_name='Подписка'
        verbose_name_plural='Подписки'

    def __str__(self):
        return self.user_name

class Lessons(models.Model):
    title=models.CharField(max_length=255, verbose_name='Название')
    text=HTMLField('Text')
    course_id = models.ForeignKey('VideoCourses', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Видеокурс')

    class Meta:
        verbose_name='Уроки'

    def __str__(self):
        return self.title

class CoursesVariants(models.Model):
    title=models.CharField(max_length=255, verbose_name='Название')
    text=HTMLField('Text')
    price=models.CharField(max_length=255, verbose_name='Цена')
    course_id = models.ForeignKey('VideoCourses', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Видеокурс')

    class Meta:
        verbose_name='Варианты курса'

    def __str__(self):
        return self.title
