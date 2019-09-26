from django.contrib import admin
from .models import Blocks, Page, VideoCourses, Events, Callback, Subscribe, Lessons, CoursesVariants,CoursesReviews, MenuBlocks, MenuItemBlocks, EventsVariants
from django import forms
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin

class MyAdminSite(AdminSite):

    def get_app_list(self, request):
        """
        Return a sorted list of all the installed apps that have been
        registered in this site.
        """
        course_app_model = ['VideoCourses', 'Events', 'Lessons']
        user_app_model = ['Subscribe', 'Callback']
        app_dict = self._build_app_dict(request)

        # Sort the apps alphabetically.
        if app_dict:
            app_dict['user_app'] = app_dict['aistsiteapp'].copy()
            app_dict['user_app']['name'] = 'Подписки/Обратная связь'
            app_dict['user_app']['app_label'] = 'callback'
            app_dict['user_app']['models'] = []
            app_dict['other_app'] = app_dict['aistsiteapp'].copy()
            app_dict['other_app']['app_label'] = 'siteapps'
            app_dict['other_app']['name'] = 'Технические разделы'
            app_dict['other_app']['models'] = []
            app_dict['course_app'] = app_dict['aistsiteapp'].copy()
            app_dict['course_app']['app_label'] = 'courses'
            app_dict['course_app']['name'] = 'Курсы/События'
            app_dict['course_app']['models'] = []
            for model in app_dict['aistsiteapp']['models']:
                if model['object_name'] in course_app_model:
                    app_dict['course_app']['models'].append(model)
                elif model['object_name'] in user_app_model:
                    app_dict['user_app']['models'].append(model)
                else:
                    app_dict['other_app']['models'].append(model)

            app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())
            # Sort the models alphabetically within each app.
            for app in app_list:
               app['models'].sort(key=lambda x: x['name'])
            return app_list

class BlocksInline(admin.StackedInline):  # instead of ModelAdmin
    model = Blocks
    extra = 1
    fields = ('tech_name', 'prior', 'name', 'text','images', 'link')

class LessonsInline(admin.StackedInline):  # instead of ModelAdmin
    model = Lessons
    extra = 1

class CoursesVariantsInline(admin.StackedInline):  # instead of ModelAdmin
    model = CoursesVariants
    extra = 1

class EventsVariantsInline(admin.StackedInline):  # instead of ModelAdmin
    model = EventsVariants
    extra = 1

class CoursesReviewsInline(admin.StackedInline):  # instead of ModelAdmin
    model = CoursesReviews
    extra = 1
    max_num = 2

class PageAdmin(admin.ModelAdmin):
	inlines = [BlocksInline]
	list_display = ('id', 'name', 'tech_title', 'published_date','slug')
	list_filter = ['published_date', 'slug']
	search_fields = ['name','tech_title','slug']

class BlocksAdmin(admin.ModelAdmin):
	inlines = [BlocksInline]

class VideoCoursesAdmin(admin.ModelAdmin):
	inlines = [LessonsInline, CoursesVariantsInline, CoursesReviewsInline]
	list_display = ('id', 'name', 'slug','prior','on_main')
	# list_filter = ['published_date', 'slug']
	# search_fields = ['name','tech_title','slug']

class EventsAdmin(admin.ModelAdmin):
	inlines = [EventsVariantsInline]
	list_display = ('id', 'name', 'slug','on_main')

class MenuItemInline(admin.TabularInline):
    model = MenuItemBlocks
    ordering = ('order',)


class MenuAdmin(admin.ModelAdmin):
    #list_display = ['name', 'slug', 'description']
    inlines = [MenuItemInline,]


admin.site = MyAdminSite()
admin.site.register(Blocks,BlocksAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(VideoCourses, VideoCoursesAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(Callback)
admin.site.register(Subscribe)
admin.site.register(Lessons)
admin.site.register(MenuBlocks, MenuAdmin)
admin.site.register(MenuItemBlocks, MenuAdmin)
# Register your models here.
