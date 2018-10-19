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

def indexView(request):
    template = loader.get_template('Demo/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def foo_view(request):
    print('GET')
    return JsonResponse("Get",safe=False)

def post_View(request):
    if request.method=='POST':
        print('POST')
        jsonData=request.POST
        print(jsonData['username'])
        print(jsonData['password'])
        return JsonResponse('1111111',  safe=False)

def savenews_View(request):
    if request.method=='POST':
        print('POST')
        jsonData=request.POST;
        content=jsonData['content']
        title=jsonData['title']
        flag=save(content=content,title=title)
        print(flag)
        return JsonResponse({'result':flag},safe=False)

def newslist_View(request):
    datatable=News.objects.all().filter()
    jsonData=serializers.serialize('json',datatable)
    print(jsonData)
    return JsonResponse(jsonData,safe=False)

def news_View(request):
    template = loader.get_template('Demo/newslist.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

@ajax
@login_required
def login_required_view(request):
    # if the request.user is anonymous then this view not proceed
    return {'user_id':request.user.id}

@ajax
def render_view(request):
    return render(request,'hello.html')

class SimpleView(TemplateView):
    template_name='hello.html'

@ajax
def exception_view(request):
    a=23/0  # this line throws an exception
    return a

@ajax
def raise_exception_view(request):
    raise Http404
