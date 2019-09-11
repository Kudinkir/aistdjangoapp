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
    text=HTMLField('Text', blank=True, null=True)
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
    about_course  = HTMLField('about_course', blank=True, null=True)
    students_results  = HTMLField('students_results', blank=True, null=True)
    on_main = models.BooleanField(blank=True,default=False,verbose_name='Выводить на главной')
    prior=models.IntegerField(verbose_name='Приоритет', default=100)

    class Meta:
        verbose_name='Видеокурс'
        verbose_name_plural='Видеокурсы'

    def __str__(self):
        return self.name

    def get_lessons_count(self):
        self.lessons = Lessons.objects.filter(course_id=self.id)
        return len(self.lessons)

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
    user_name=models.CharField(max_length=255, verbose_name='Имя пользователя',blank=True)
    email = models.EmailField(max_length=255,blank=True)
    text=models.TextField(blank=True, verbose_name='Неделя беременности',choices=STATUS)
    amount=models.IntegerField(verbose_name='Неделя беременности', default=100)
    personal_agree=models.BooleanField(default=True)

    class Meta:
        verbose_name='Подписка'
        verbose_name_plural='Подписки'

    def __str__(self):
        return self.email

class Lessons(models.Model):
    title=models.CharField(max_length=255, verbose_name='Название')
    text=HTMLField('Text')
    duration=models.CharField(max_length=255, verbose_name='Длительность, 1 час',blank=True,)
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
                    item.childrens = VideoCourses.objects.all()
                elif item.display_event:
                    item.childrens = Events.objects.all()
                childrens = MenuItemBlocks.objects.filter(menu_item_id=item.id)
                if len(childrens):
                    print(childrens[0].link_url)
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
