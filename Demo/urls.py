from django.urls import path
from . import views,funcView

app_name='Demo'
urlpatterns=[
    path('',views.indexView,name='index'),
    path('foo',views.foo_view,name='foo'),
    path('post',views.post_View,name='post'),
    path('savenews',views.savenews_View,name='savenews'),
    path('newslist/<int:year>',funcView.newslist_View,name='newslist'),
    path('news',views.news_View,name='news'),
    path('addAdv',funcView.addAdv_View,name='addAdv'),
    path('addAdv/newAdv',funcView.newAdv_View,name='newAdv'),
    path('addAdv/newAdv&<str:name>',funcView.newAdvName_View,name='newAdv&name')
]