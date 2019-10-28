from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from tinymce.models import HTMLField
from django.utils.text import slugify
from pytils.translit import slugify
from datetime import date


class Page(models.Model):
    name =models.CharField(max_length=255, blank=True, null=True)
    seo_title = models.CharField(max_length=255, blank=True, null=True)
    tech_title = models.CharField(max_length=255, blank=True, null=True, verbose_name='Техническое название')
    seo_description = models.CharField(max_length=255, blank=True, null=True)
    seo_keywords = models.CharField(max_length=255, blank=True, null=True)
    published_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255,  blank=True, null=True)

    class Meta:
        verbose_name='Страницы'
        verbose_name_plural='Страницы'

    def __str__(self):
        return self.name


class Blocks(models.Model):
    tech_name=models.CharField(max_length=255, blank=True, null=True, unique=True,verbose_name='Техническое имя')
    prior=models.IntegerField(verbose_name='Приоритет', default=100)
    name=models.CharField(max_length=255)
    block_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name='id Block')
    page_id = models.ForeignKey('Page', on_delete=models.CASCADE, blank=True, null=True, verbose_name='related Page')
    text=HTMLField('Text', blank=True, null=True)
    images = models.ImageField(upload_to='images/', blank=True)
    link = models.CharField(max_length=255, blank=True, null=True,verbose_name='Ссылка в блоке(youtube, insta, or other)')

    class Meta:
        verbose_name='Блок'
        verbose_name_plural='Блоки'

    def __str__(self):
        return self.name

class VideoCourses(models.Model):
    on_main = models.BooleanField(blank=True,default=False,verbose_name='Выводить на главной')
    visible = models.BooleanField(blank=True,default=False,verbose_name='Видимость')
    prior=models.IntegerField(verbose_name='Приоритет', default=100)
    name=models.CharField(max_length=255)
    lessons_number = models.CharField(max_length=255,blank=True, null=True,verbose_name='Кол-во уроков')
    duration_number = models.CharField(max_length=255,blank=True, null=True,verbose_name='Кол-во часов')
    video =  models.CharField(max_length=255,  blank=True, null=True)
    slug = models.CharField(max_length=255,  blank=True, null=True, verbose_name='URL')
    images = models.ImageField(upload_to='images/', blank=True)
    text=HTMLField('Текст')
    students_results  = HTMLField('Результаты студентов', blank=True, null=True)
    about_course  = HTMLField('О курсе', blank=True, null=True)
    second_text = HTMLField('Дополнительный текст',blank=True, null=True)


    class Meta:
        verbose_name='Видеокурс'
        verbose_name_plural='Видеокурсы'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if(not self.slug):
            slug=slugify(self.name)
            self.slug = slug
        super(VideoCourses, self).save(*args, **kwargs)

class VideoBlocks(models.Model):
    tech_name=models.CharField(max_length=255, blank=True, null=True, unique=True,verbose_name='Техническое имя')
    prior=models.IntegerField(verbose_name='Приоритет', default=100)
    name=models.CharField(max_length=255)
    videocourse_id = models.ForeignKey('VideoCourses', on_delete=models.CASCADE, blank=True, null=True, verbose_name='id Видеокурса')
    text=HTMLField('Text', blank=True, null=True)
    images = models.ImageField(upload_to='images/', blank=True)
    link = models.CharField(max_length=255, blank=True, null=True,verbose_name='Ссылка в блоке')

    class Meta:
        verbose_name='Блок Видеокурса'
        verbose_name_plural='Блоки Видеокурсов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if(not self.tech_name):
            tech_name=slugify(self.name)
            self.tech_name = tech_name
        super(VideoBlocks, self).save(*args, **kwargs)

class Events(models.Model):
    on_main = models.BooleanField(blank=True,default=False,verbose_name='Выводить на главной')
    visible = models.BooleanField(blank=True,default=False,verbose_name='Видимость')
    name=models.CharField(max_length=255, blank=True)
    images = models.ImageField(upload_to='images/', blank=True)
    video =  models.CharField(max_length=255,  blank=True, null=True)
    slug = models.CharField(max_length=255,  blank=True, null=True)
    text=HTMLField('Text')
    prior=models.IntegerField(verbose_name='Приоритет', default=100)
    start_date=models.DateTimeField(blank=True, default=now)
    place =  models.CharField(max_length=255,  blank=True, null=True,verbose_name='Место проведения')

    class Meta:
        verbose_name='Событие'
        verbose_name_plural='События'

    def __str__(self):
        return self.name

class Callback(models.Model):
    user_name=models.CharField(max_length=255, blank=True, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=255)
    text=HTMLField('Text')
    personal_agree=models.BooleanField(default=True)
    published_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='Обратная связь'
        verbose_name_plural='Обратная связь'

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
    user_name=models.CharField(max_length=255, verbose_name='Имя пользователя',blank=True)
    email = models.EmailField(max_length=255,unique=True,default='empty@emty.ru')
    text=models.TextField(blank=True, verbose_name='Срок беременности',choices=STATUS)
    amount=models.IntegerField(verbose_name='Неделя беременности', default=100)
    personal_agree=models.BooleanField(default=True)
    published_date = models.DateTimeField(blank=True,null=True, verbose_name='Дата регистрации')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name='Подписка'
        verbose_name_plural='Подписки'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # if(not self.text):
        text = '1-11';
        if(self.amount > 11 and self.amount <=19):
            text = '12-19'
        if(self.amount > 19 and self.amount <=29):
            text = '20-29'
        if(self.amount > 29 and self.amount <=41):
            text = '30-41'
        if(self.amount > 41):
            text = 'После родов'
        self.text = text
        if(not self.published_date):
            self.published_date = now()
        super(Subscribe, self).save(*args, **kwargs)

class Lessons(models.Model):
    title=models.CharField(max_length=255, blank=True, verbose_name='Название')
    text=HTMLField('Text')
    #duration=models.CharField(max_length=255, verbose_name='Длительность',blank=True,)
    course_id = models.ForeignKey('VideoCourses', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Видеокурс')

    class Meta:
        verbose_name='Урок'
        verbose_name_plural='Уроки'

    def __str__(self):
        return self.title

class EventsProgrammItem(models.Model):
    title=models.CharField(max_length=255,blank=True, verbose_name='Название')
    text=HTMLField('Text')
    duration=models.CharField(max_length=255, verbose_name='Длительность, 1 час',blank=True,)
    course_id = models.ForeignKey('Events', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Семинар')

    class Meta:
        verbose_name='Часть Семинара'
        verbose_name_plural='Части Семинара'

    def __str__(self):
        return self.title

class CoursesVariants(models.Model):
    title=models.CharField(max_length=255, blank=True, null=True, verbose_name='Название')
    text=HTMLField('Text')
    price=models.CharField(max_length=255, blank=True, verbose_name='Цена')
    price_link=models.TextField(verbose_name='id товара',blank=True, null=True,)
    course_id = models.ForeignKey('VideoCourses', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Видеокурс')

    class Meta:
        verbose_name='Вариант курса'
        verbose_name_plural='Варианты курса'

    def __str__(self):
        return self.title

class EventsVariants(models.Model):
    title=models.CharField(max_length=255, verbose_name='Название', blank=True)
    text=HTMLField('Text')
    price=models.CharField(max_length=255, blank=True, verbose_name='Цена')
    price_link=models.CharField(max_length=255, verbose_name='id товара',blank=True, null=True,)
    course_id = models.ForeignKey('Events', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Семинар')

    class Meta:
        verbose_name='Вариант Семинара'
        verbose_name_plural='Варианты Семинара'

    def __str__(self):
        return self.title

class CoursesReviews(models.Model):
    title=models.CharField(max_length=255, blank=True,verbose_name='Заголовок')
    text=HTMLField('Text')
    autor=models.CharField(max_length=255, blank=True,verbose_name='Автор')
    image=models.ImageField(upload_to='images/', blank=True)
    course_id = models.ForeignKey('VideoCourses', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Видеокурс')

    class Meta:
        verbose_name='Отзыв о курсе'
        verbose_name_plural='Отзывы о курсе'

    def __str__(self):
        return self.title

class EventsReviews(models.Model):
    title=models.CharField(max_length=255, verbose_name='Заголовок', blank=True)
    text=HTMLField('Text')
    autor=models.CharField(max_length=255, verbose_name='Автор', blank=True)
    image=models.ImageField(upload_to='images/', blank=True)
    video=models.CharField(max_length=255, blank=True, verbose_name='Ссылка на видео')
    course_id = models.ForeignKey('Events', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Семинар')

    class Meta:
        verbose_name='Отзыв о семинаре'
        verbose_name_plural='Отзывы о семинаре'

    def __str__(self):
        return self.title

class EventsPlaces(models.Model):
    on_main = models.BooleanField(blank=True,default=False,verbose_name='Выводить на главной в кружочке')
    city=models.CharField(max_length=255, verbose_name='Место проведения', blank=True)
    visible = models.BooleanField(blank=True,default=False,verbose_name='Видимость')
    start_date=models.DateTimeField(blank=True, default=now)
    course_id = models.ForeignKey('Events', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Семинар')

    class Meta:
        verbose_name='Место проведения'
        verbose_name_plural='Места проведения'

    # def __str__(self):
    #     return self.course_id

class MenuBlocks(models.Model):
        name = models.CharField(max_length=100)
        slug = models.TextField()
        description = models.TextField(blank=True,null=True)

        class Meta:
            verbose_name = 'Меню'
            verbose_name_plural = 'Меню'

        def __str__(self):
            return self.name

        def get_items(self):
            self.items = MenuItemBlocks.objects.filter(menu_id=self.id)
            for item in self.items:
                if item.display_video:
                    item.childrens = VideoCourses.objects.filter(visible=True)
                elif item.display_event:
                    item.childrens = EventsPlaces.objects.filter(visible=True,start_date__gte=date.today())
                    for place in item.childrens:
                        place.title = place.city + ' '
                        place.start_date = place.start_date
                        place.slug = place.course_id.slug
                childrens = MenuItemBlocks.objects.filter(menu_item_id=item.id)
                if len(childrens):
                    item.childrens = childrens
            return self.items


class MenuItemBlocks(models.Model):
        menu = models.ForeignKey(MenuBlocks,verbose_name='Имя',on_delete=models.CASCADE,blank=True,null=True)
        menu_item = models.ForeignKey('self',verbose_name='Имя',on_delete=models.CASCADE,blank=True,null=True)
        order = models.IntegerField(verbose_name='Приоритет',default=500)
        link_url = models.CharField(
            max_length=100,
            help_text='URL or URI to the content, eg /about/ or http://foo.com/'
            )
        title = models.CharField(max_length=100)
        display_video = models.BooleanField(blank=True,default=False,)
        display_event = models.BooleanField(blank=True,default=False,)

        class Meta:
            verbose_name = 'Пункт меню'
            verbose_name_plural = 'Пункты меню'

        def __str__(self):
            return self.title
