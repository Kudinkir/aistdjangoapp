from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from aistsiteapp.models import Blocks, Page, VideoCourses, Events, Lessons, CoursesVariants
from aistsiteapp.forms import SubscribeForm, CallbackForm
from datetime import date

# Create your views here.
def home(request):
    subscribe_form = SubscribeForm()
    page = Page.objects.get(tech_title='main_page')
    main_block = Blocks.objects.get(id=1)
    second_block = Blocks.objects.get(id=2)
    second_block.bloks = Blocks.objects.filter(block_id=2)
    event_block = Events.objects.filter(start_date__gte=date.today())
    courses_block = VideoCourses.objects.all()
    footer_block = Blocks.objects.get(id=7)
    footer_block.bloks = Blocks.objects.filter(block_id=7)
    return render(request, 'aistsiteapp/main.html', {
        'page_info' : page,
        'main_block' : main_block,
        'second_block' : second_block,
        'footer_block' : footer_block,
        'form': subscribe_form,
        'event_block': event_block,
        #'courses_block': courses_block
    })

def videocourses(request):
    footer_block = Blocks.objects.get(id=7)
    footer_block.bloks = Blocks.objects.filter(block_id=7)
    videocourses = VideoCourses.objects.all()
    return render(request, 'aistsiteapp/videocourses.html', {
        'videocourses' : videocourses,
        'footer_block' : footer_block,
    })

def videocourses_item(request, slug):
    footer_block = Blocks.objects.get(id=7)
    footer_block.bloks = Blocks.objects.filter(block_id=7)
    videocourse = VideoCourses.objects.get(slug=slug)
    videocourse.lessons = Lessons.objects.filter(course_id=videocourse.id)
    videocourse.variants = CoursesVariants.objects.filter(course_id=videocourse.id)
    return render(request, 'aistsiteapp/videocourses_item.html', {
        'videocourse' : videocourse,
        'footer_block' : footer_block,
    })

def events(request):
    footer_block = Blocks.objects.get(id=7)
    footer_block.bloks = Blocks.objects.filter(block_id=7)
    events = Events.objects.all()
    return render(request, 'aistsiteapp/events.html', {
        'events' : events,
        'footer_block' : footer_block,
    })

def events_item(request, slug):
    footer_block = Blocks.objects.get(id=7)
    footer_block.bloks = Blocks.objects.filter(block_id=7)
    event = get_object_or_404(Events, slug=slug)
    return render(request, 'aistsiteapp/events_item.html', {
        'event' : event,
        'footer_block' : footer_block,
    })

def pages(request, slug):
    footer_block = Blocks.objects.get(id=7)
    footer_block.bloks = Blocks.objects.filter(block_id=7)
    page = get_object_or_404(Page, slug=slug)
    blocks = Blocks.objects.filter(page_id=page.id)
    return render(request, 'aistsiteapp/page.html', {
        'page' : page,
        'blocks' : blocks,
        'footer_block' : footer_block,
    })

def subscribe(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'errors': 0})
    else:
        return JsonResponse({'errors': 'Use post method!'})

def callback(request):
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'errors': 0})
    else:
        return JsonResponse({'errors': 'Use post method!'})
