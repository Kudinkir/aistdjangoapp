from django.http import request
from aistsiteapp.models import Blocks, Page, VideoCourses, Events, Lessons, CoursesVariants,MenuBlocks,MenuItemBlocks
from datetime import date

def menu(request):
    event_block = Events.objects.filter(start_date__gte=date.today())
    courses_block = VideoCourses.objects.all()
    main_menu = MenuBlocks.objects.get(slug='top_menu')
    main_menu.items = main_menu.get_items()
    footer_menu = MenuBlocks.objects.get(slug='bottom_menu')
    footer_menu.items = footer_menu.get_items()
    return {
        'footer_menu' : footer_menu,
        'event_block'  : event_block,
        'courses_block'  : courses_block,
        'main_menu' : main_menu
    }
