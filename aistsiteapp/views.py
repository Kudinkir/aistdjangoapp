from django.shortcuts import render
from aistsiteapp.models import Blocks, Page, VideoCourses

# Create your views here.
def home(request):
    page = Page.objects.get(tech_title='main_page')
    main_block = Blocks.objects.get(id=1)
    second_block = Blocks.objects.get(id=2)
    second_block.bloks = Blocks.objects.filter(block_id=2)
    return render(request, 'aistsiteapp/main.html', {
        'page_info' : page,
        'main_block' : main_block,
        'second_block' : second_block,
    })

def videocourses(request):
    page = Page.objects.get(tech_title='main_page')
    #blocks = Blocks.objects.get(page_id=1)
    return render(request, 'aistsiteapp/videocourses.html', {
        'page_info' : page,
        'blocks' : blocks
    })
