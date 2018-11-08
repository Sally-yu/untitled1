from django.urls import path
from . import views

app_name='Demo'
urlpatterns=[
    path('',views.indexView,name='index'),
    path('newsDetail')
]