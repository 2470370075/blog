from django import template
from app01 import models
from django.db.models import Count

register = template.Library()


@register.inclusion_tag('left.html')
def get_left_block(username):
    user = models.UserInfo.objects.filter(username=username)[0]
    time = models.Article.objects.filter(user=user).extra(
        select={'t': "date_format(create_time,'%%Y-%%m')"}
    ).values('t').annotate(c=Count('nid')).values('t', 'c')

    ret2 = models.Category.objects.all()
    article = {}
    for i in ret2:
        ret3 = i.article_set.all().filter(user=user).count()
        if ret3 != 0:
            article[i.title] = ret3

    tag = models.Article.objects.filter(user=user).values('tag__tagtitle').annotate(c=Count('tag__tagtitle')).values(
        'tag__tagtitle', 'c')

    return {
        'd': article,
        'time': time,
        'ret4': tag
    }
