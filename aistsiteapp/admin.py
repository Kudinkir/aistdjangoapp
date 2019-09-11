from django.contrib import admin
from .models import  Blocks, Page, VideoCourses, Events, Callback, Subscribe, Lessons, CoursesVariants, MenuBlocks, MenuItemBlocks
from django import forms

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

class BlocksAdmin(admin.ModelAdmin):
	inlines = [BlocksInline]

class VideoCoursesAdmin(admin.ModelAdmin):
	inlines = [LessonsInline, CoursesVariantsInline]
	# list_display = ('id', 'name', 'tech_title', 'published_date','slug')
	# list_filter = ['published_date', 'slug']
	# search_fields = ['name','tech_title','slug']

class MenuItemInline(admin.TabularInline):
    model = MenuItemBlocks
    ordering = ('order',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    inlines = [MenuItemInline,]

admin.site.register(Blocks,BlocksAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(VideoCourses, VideoCoursesAdmin)
admin.site.register(Events)
admin.site.register(Callback)
admin.site.register(Subscribe)
admin.site.register(Lessons)
admin.site.register(MenuBlocks, MenuAdmin)
# Register your models here.
