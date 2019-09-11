from django.http import request
from aistsiteapp.models import Blocks, Page, VideoCourses, Events, Lessons, CoursesVariants
from datetime import date

def menu(request):
    event_block = Events.objects.filter(start_date__gte=date.today())
    courses_block = VideoCourses.objects.all()
    footer_block = Blocks.objects.get(id=7)
    footer_block.bloks = Blocks.objects.filter(block_id=7)
    return {
        'footer_block' : footer_block,
        'event_block'  : event_block,
        'courses_block'  : courses_block,
    }
