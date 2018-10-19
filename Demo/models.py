import uuid
from django.contrib.auth.hashers import make_password, check_password
from django.db import models

# Create your models here.


#用户
class User(models.Model):
    sexChoice=(
                  ('0','男'),
                  ('1','女'),
                  ('2','保密')
    )
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    code=models.CharField('编号',max_length=20,unique=True)
    name=models.CharField('昵称',max_length=200,unique=True)
    createTime=models.DateTimeField('创建时间',auto_now_add=True)#创建时自动赋值一次
    email=models.CharField('邮箱',max_length=200,unique=True)
    phone=models.CharField('电话',max_length=200,unique=True)
    sex=models.CharField('性别',choices=sexChoice,max_length=10)
    birthday=models.DateField('生日',null=True,blank=True)
    level=models.IntegerField('等级',editable=False,default=0)
    password=models.CharField('密码',max_length=50)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='用户'
        verbose_name='用户'

#新闻
class News(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    title=models.CharField('标题',max_length=200)
    content=models.TextField('内容',max_length=2048)
    author=models.ForeignKey(User,verbose_name='作者',on_delete=models.DO_NOTHING(None,None,None,None),null=True,blank=True)
    pubTime=models.DateTimeField('发布时间',auto_now_add=True,null=True,blank=True)#创建时自动赋值
    modifyTime=models.DateTimeField('最后修改时间',auto_now=True)#保存时更新最后修改时间
    url=models.URLField('路径',null=True,blank=True)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='新闻'
        verbose_name_plural='新闻'




#各种设置的参数
class Option(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    paramName=models.CharField('参数名',unique=True,max_length=50)
    group=models.CharField('组',max_length=50,blank=True)
    value=models.CharField('值',max_length=1024)
    enable=models.BooleanField('有效',default=True)
    readonly=models.BooleanField('只读',default=False,null=False)

    def __str__(self):
        return self.paramName+': '+self.value

    class Meta:
        verbose_name='参数'
        verbose_name_plural='设置'