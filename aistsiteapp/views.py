from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from aistsiteapp.models import Blocks, Page, VideoCourses, Events, Lessons, CoursesVariants,CoursesReviews
from aistsiteapp.forms import SubscribeForm, CallbackForm
from datetime import date

# Create your views here.
def home(request):
    subscribe_form = SubscribeForm()
    page = Page.objects.get(tech_title='main_page')
    main_block = Blocks.objects.get(id=1)
    second_block = Blocks.objects.get(id=2)
    second_block.bloks = Blocks.objects.filter(block_id=2)
    videocourses_main = VideoCourses.objects.order_by('prior').filter(on_main=True)
    events_main = Events.objects.order_by('prior').filter(on_main=True)
    instagram_block = Blocks.objects.get(tech_name='insta_block')
    youtube_block = Blocks.objects.get(tech_name='youtube_block')
    for course in videocourses_main:
        course.slug = "video-courses/"+course.slug
        course.lessons = Lessons.objects.filter(course_id=course.id)
    return render(request, 'aistsiteapp/main.html', {
        'page_info' : page,
        'main_block' : main_block,
        'second_block' : second_block,
        'form': subscribe_form,
        'videocourses_main': videocourses_main,
        'events_main': events_main,
        'instagram_block' : instagram_block,
        'youtube_block' : youtube_block,
    })

def videocourses(request):
    videocourses = VideoCourses.objects.all()
    return render(request, 'aistsiteapp/videocourses.html', {
        'videocourses' : videocourses,
    })

def videocourses_item(request, slug):
    videocourse = VideoCourses.objects.get(slug=slug)
    videocourse.lessons = Lessons.objects.filter(course_id=videocourse.id)
    videocourse.variants = CoursesVariants.objects.filter(course_id=videocourse.id)
    videocourse.reviews = CoursesReviews.objects.filter(course_id=videocourse.id)
    other_courses = VideoCourses.objects.exclude(id=videocourse.id)
    return render(request, 'aistsiteapp/videocourses_item.html', {
        'videocourse' : videocourse,
        'other_courses' : other_courses,
    })

def events(request):
    events = Events.objects.all()
    return render(request, 'aistsiteapp/events.html', {
        'events' : events,
    })

def events_item(request, slug):
    event = get_object_or_404(Events, slug=slug)
    return render(request, 'aistsiteapp/events_item.html', {
        'event' : event,
    })

def pages(request, slug):
    page = get_object_or_404(Page, slug=slug)
    blocks = Blocks.objects.filter(page_id=page.id)
    return render(request, 'aistsiteapp/page.html', {
        'page' : page,
        'blocks' : blocks,
    })

def subscribe(request):
    errors = 1
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            errors = 0
    return JsonResponse({'errors': errors})

def callback(request):
    if request.method == "POST":
        form = CallbackForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'errors': 0})
    else:
        return JsonResponse({'errors': 'Use post method!'})
