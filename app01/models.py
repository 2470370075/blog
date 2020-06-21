from django.db import models
import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):

    nid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11, null=True, unique=True,blank=True)
    avatar = models.FileField(upload_to="avatars/",null=True, verbose_name="头像")
    create_time = models.DateTimeField(null=True,auto_now_add=True)
    blog=models.ForeignKey(to='Blog',to_field="nid", null=True)


class Article(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(null=True,max_length=20,)
    abstract=models.CharField(null=True,max_length=200,)
    user = models.ForeignKey(null=True,to="UserInfo", to_field="nid")
    create_time = models.DateTimeField(null=True,auto_now_add=True)
    comment=models.IntegerField(default=0,)
    down = models.IntegerField(default=0, )
    up = models.IntegerField(default=0, )
    blog = models.ForeignKey(null=True, to='Blog', to_field='nid')
    category = models.ForeignKey(null=True, to='Category', to_field='nid')
    tag=models.ManyToManyField(to='Tag',)
    detail=models.OneToOneField(null=True,to='Detail',to_field='nid')

    def __str__(self):
        return self.title


class Detail(models.Model):
    nid=models.AutoField(primary_key=True)
    detail=models.TextField()

    def __str__(self):
        return self.detail

class Blog(models.Model):
    nid=models.AutoField(primary_key=True)
    blogtitle=models.CharField(null=True,max_length=20,)
    theme=models.CharField(null=True,max_length=20)

    def __str__(self):
        return self.blogtitle


class Category(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(null=True,max_length=20)

    def __str__(self):
        return self.title


class Tag(models.Model):
    nid=models.AutoField(primary_key=True)
    tagtitle=models.CharField(null=True,max_length=20,)

    def __str__(self):
        return self.tagtitle



class Updown(models.Model):
    nid=models.AutoField(primary_key=True)
    user=models.CharField(null=True,max_length=20,)
    article=models.CharField(null=True,max_length=20,)
    updown=models.BooleanField(default=True)

    class Meta:
        unique_together=('user','article')


class Comments(models.Model):
    nid = models.AutoField(primary_key=True)
    user=models.ForeignKey(to='UserInfo',null=True)
    article=models.ForeignKey(to='Article',null=True)
    context=models.CharField(null=True,max_length=100,)
    createtime=models.DateTimeField(null=True,auto_now_add=True)
    pid=models.ForeignKey('self',null=True,)


class Problem(models.Model):
    info=models.CharField(null=True,max_length=2000)