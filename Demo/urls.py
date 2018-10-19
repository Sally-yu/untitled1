from django.urls import path
from . import views

app_name='Demo'
urlpatterns=[
    path('',views.indexView,name='index'),
    path('foo',views.foo_view,name='foo'),
    path('post',views.post_View,name='post'),
    path('savenews',views.savenews_View,name='savenews'),
]