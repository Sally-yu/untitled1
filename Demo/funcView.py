import json
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.template import loader
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import Http404,HttpResponse,JsonResponse
from django_ajax.decorators import ajax

from Demo.models import News
from .func import save

# We're using `django_ajax.middleware.AJAXMiddleware` in settings
# so we don't need to use `@ajax` and `AJAXMixin` decorators

#Unsafe mode JsonResponse
def CusResponse(data):
    return JsonResponse(data,safe=False);

def indexView(request):
    template = loader.get_template('Demo/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def foo_view(request):
    print('GET')
    return CusResponse("get")

def post_View(request):
    if request.method=='POST':
        print('POST')
        jsonData=request.POST
        print(jsonData['username'])
        print(jsonData['password'])
        return CusResponse('right user')

def savenews_View(request):
    if request.method=='POST':
        print('POST')
        jsonData=request.POST;
        content=jsonData['content']
        title=jsonData['title']
        flag=save(content=content,title=title)
        print(flag)
        return CusResponse({'result':flag})

def newslist_View(request,year):
    datatable=News.objects.all().filter()
    jsonData=serializers.serialize('json',datatable)
    print(jsonData)
    print(year)
    return CusResponse(jsonData)

def news_View(request):
    template = loader.get_template('Demo/newslist.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
