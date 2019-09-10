from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import  Blocks, Page, VideoCourses, Events, Callback, Subscribe, Lessons, CoursesVariants
from django_summernote.widgets import SummernoteWidget


class BloksModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'

class BlocksInline(admin.StackedInline):  # instead of ModelAdmin
    model = Blocks
    fields = ('tech_name', 'prior', 'name', 'text','images')

class LessonsInline(admin.StackedInline):  # instead of ModelAdmin
    model = Lessons

class CoursesVariantsInline(admin.StackedInline):  # instead of ModelAdmin
    model = CoursesVariants

class PageAdmin(admin.ModelAdmin):
	inlines = [BlocksInline]
	list_display = ('id', 'name', 'tech_title', 'published_date','slug')
	list_filter = ['published_date', 'slug']
	search_fields = ['name','tech_title','slug']


class VideoCoursesAdmin(admin.ModelAdmin):
	inlines = [LessonsInline, CoursesVariantsInline]
	# list_display = ('id', 'name', 'tech_title', 'published_date','slug')
	# list_filter = ['published_date', 'slug']
	# search_fields = ['name','tech_title','slug']

admin.site.register(Blocks,BloksModelAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(VideoCourses,VideoCoursesAdmin)
admin.site.register(Events,BloksModelAdmin)
admin.site.register(Callback)
admin.site.register(Subscribe)
admin.site.register(Lessons)
# Register your models here.
