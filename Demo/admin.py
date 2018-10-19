from django.contrib import admin

from .models import News,User,Option

# admin.site.site_header='后台管理系统'
# admin.site.site_title='Demo'

#自定义的管理页面和路径，路径在urls
class MyAdminSite(admin.AdminSite):
    site_title = '管理系统'
    site_header = '后台管理系统'

admin_site=MyAdminSite(name='Management')

# Register your models here.
class newsAdmin(admin.ModelAdmin):
    list_display = ['title','pubTime','modifyTime']
    ordering = ['-modifyTime'] #排序

    #筛选器
    list_filter = ['modifyTime','pubTime']
    search_fields = ['title']
    date_hierarchy = 'pubTime'    # 详细时间分层筛选　

    fieldsets = (
        ('必填',{'fields':['title','content']}),
        #('非必填',{'fields':[('author','url')]}),#同行显示
        ('非必填',{'fields':['author','url']}),
    )

    #重写保存前
    def save_model(self, request, obj, form, change):
        if change: #修改时
            pass
        else: #新增时
            pass
        super(newsAdmin,self).save_model(request,obj,form,change)

    # 重写删除
    def delete_model(self, request, obj):
        super(newsAdmin,self).delete_model(request,obj)


class userAdmin(admin.ModelAdmin):
    list_display = ['name','code','birthday','level']
    search_fields = ['name','code']

class optionAdmin(admin.ModelAdmin):
    list_display = ['paramName','value','enable']
    search_fields = ['paraName']

admin_site.register(User,userAdmin)
admin_site.register(News,newsAdmin)
admin_site.register(Option,optionAdmin)