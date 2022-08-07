
from unicodedata import name
from django.urls import path

import base.views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/', views.post, name='post')
]
