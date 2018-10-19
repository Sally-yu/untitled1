from .models import News

def save(content,title):
    news=News.objects.all()
    set=news.filter(title=title)
    if set.count()>=1:
        return '标题重复'
    news.create(content=content,title=title)
    return '保存成功'