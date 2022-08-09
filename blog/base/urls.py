
from unicodedata import name
from django.urls import path

import base.views as views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.post, name='post')
]
