from django.urls import path
from main.views import *
from django.urls import re_path

urlpatterns = [
    path('',show,name='show_page'),
    path('add/',add,name='add_page'),
    re_path(r'^complete/<(?P<article_id>\d+)/$:id>',complete_un,name='complete_un_task')
]
