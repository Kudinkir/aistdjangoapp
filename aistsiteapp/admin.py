from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import  Blocks, Page, VideoCourses, Events

class BloksModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'
        
admin.site.register(Blocks,BloksModelAdmin)
admin.site.register(Page)
admin.site.register(VideoCourses,BloksModelAdmin)
admin.site.register(Events,BloksModelAdmin)
# Register your models here.
