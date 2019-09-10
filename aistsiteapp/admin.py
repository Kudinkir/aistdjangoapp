from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import  Blocks, Page, VideoCourses, Events, Callback, Subscribe

class BloksModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'

class BlocksInline(admin.StackedInline):  # instead of ModelAdmin
        model = Blocks
        fields = ('tech_name', 'prior', 'name', 'text','images')

class PageAdmin(admin.ModelAdmin):
	inlines = [BlocksInline]
	list_display = ('id', 'name', 'tech_title', 'published_date','slug')
	list_filter = ['published_date', 'slug']
	search_fields = ['name','tech_title','slug']

admin.site.register(Blocks,BloksModelAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(VideoCourses,BloksModelAdmin)
admin.site.register(Events,BloksModelAdmin)
admin.site.register(Callback)
admin.site.register(Subscribe)
# Register your models here.
