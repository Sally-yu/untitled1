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

#JsonResponse without safe
def CusResponse(data,safeOrNot=False):
    return JsonResponse(data,safe=safeOrNot)



#index with news list
def indexView(request):
    template = loader.get_template('Demo/index.html')
    datatable=News.objects.all().filter()
    jsonData=serializers.serialize('json',datatable)
    print(jsonData)
    context = {
        'data':json
    }
    return HttpResponse(template.render(context, request))


#news detail view
def detailView(request):
    template=loader.get_template('Demo/detail.html')
    context={}
    return HttpResponse(template.render(context, request))



#add new news view
@login_required
def addDetailView(request):
    template=loader.get_template('Demo/addDetail.html')
    context={}
    return HttpResponse(template.render(context,request))




#save or cant save
@login_required
def saveDetailView(request):
    if request.method=='POST':
        jsonData=request.POST;
        content=jsonData['content']
        title=jsonData['title']
        flag=save(content=content,title=title)
        print(flag)
        return CusResponse({'result':flag})



#test
def post_View(request):
    if request.method=='POST':
        print('POST')
        jsonData=request.POST
        print(jsonData['username'])
        print(jsonData['password'])
        return JsonResponse('1111111',  safe=False)




#返回保存结果，不跳转
@login_required
def savenews_View(request):
    if request.method=='POST':
        print('POST')
        jsonData=request.POST;
        content=jsonData['content']
        title=jsonData['title']
        flag=save(content=content,title=title)   #处理保存后的结果
        print(flag)
        return CusResponse({'result':flag})




