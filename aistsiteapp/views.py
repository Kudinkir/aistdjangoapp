from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from aistsiteapp.models import Blocks, Page, VideoCourses, Events
from aistsiteapp.forms import SubscribeForm, CallbackForm

# Create your views here.
def home(request):
    subscribe_form = SubscribeForm()
    page = Page.objects.get(tech_title='main_page')
    main_block = Blocks.objects.get(id=1)
    second_block = Blocks.objects.get(id=2)
    second_block.bloks = Blocks.objects.filter(block_id=2)
    footer_block = Blocks.objects.get(id=7)
    footer_block.bloks = Blocks.objects.filter(block_id=7)
    return render(request, 'aistsiteapp/main.html', {
        'page_info' : page,
        'main_block' : main_block,
        'second_block' : second_block,
        'footer_block' : footer_block,
        'form': subscribe_form
    })

def videocourses(request):
    videocourses = VideoCourses.objects.all()
    return render(request, 'aistsiteapp/videocourses.html', {
        'videocourses' : videocourses,
    })

def videocourses_item(request, slug):
    videocourse = VideoCourses.objects.get(slug=slug)
    return render(request, 'aistsiteapp/videocourses_item.html', {
        'videocourse' : videocourse
    })

def events(request):
    events = Events.objects.all()
    return render(request, 'aistsiteapp/events.html', {
        'events' : events,
    })

def events_item(request, slug):
    event = get_object_or_404(Events, slug=slug)
    return render(request, 'aistsiteapp/events_item.html', {
        'event' : event
    })

def pages(request, slug):
    page = get_object_or_404(Page, slug=slug)
    blocks = Blocks.objects.filter(page_id=page.id)
    return render(request, 'aistsiteapp/page.html', {
        'page' : page,
        'blocks' : blocks
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
