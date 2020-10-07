from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('achievements', views.achievements, name='achievements'),
    path('contact', views.contact, name='contact'),
    path('send', views.ContactCreateView, name='send')
]
