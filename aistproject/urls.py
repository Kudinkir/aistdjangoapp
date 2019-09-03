"""aistproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aistsiteapp import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.home, name='home'),
    path('video-courses/', views.videocourses, name='videocourses'),
    path('video-courses/<str:slug>', views.videocourses_item, name='videocourses_item'),
    path('events/', views.events, name='events'),
    path('events/<str:slug>', views.events_item, name='events_item'),
    path('<str:slug>', views.pages, name='pages'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
