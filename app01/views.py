from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from app01 import models
from app01 import form
from geetest import GeetestLib
from django.contrib import auth
from django.db.models import Count,F
import json
import os
from untitled6 import settings
from bs4 import BeautifulSoup


VALID_CODE = ""
pc_geetest_id = "b46d1900d0a894591916ea94ea91bd2c"
pc_geetest_key = "36fc3fe98530eea08dfc6ce76e3d24c4"

def get_geetest(request):
    user_id = 'test'
    gt = GeetestLib(pc_geetest_id, pc_geetest_key)
    status = gt.pre_process(user_id)
    request.session[gt.GT_STATUS_SESSION_KEY] = status
    request.session["user_id"] = user_id
    response_str = gt.get_response_str()
    return HttpResponse(response_str)

def loginout(request):
    auth.logout(request)
    return render(request,'login.html')

def registe(request):
    reform=form.Reform()
    if request.method=='POST':
        ret={'status':0,'msg':''}
        reform=form.Reform(request.POST)
        if reform.is_valid():
            reform.cleaned_data.pop('password2')
            avater1=request.FILES.get("avatar")
            user = models.UserInfo.objects.create_user(**reform.cleaned_data,avatar=avater1)
            auth.login(request, user)
            ret['msg']="/index/"
            return JsonResponse(ret)
        else:
            ret['status']=1
            ret['msg']=reform.errors
            return JsonResponse(ret)
    return render(request,'registe2.html',{'reform':reform})

def check_username(request):
    if request.method=='GET':
        data={'status':0}
        username=request.GET.get('username')
        is_exist=models.UserInfo.objects.filter(username=username)
        if is_exist:
            data['status']=1
        return JsonResponse(data)

def login(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        username = request.POST.get("username")
        pwd = request.POST.get("password")
        gt = GeetestLib(pc_geetest_id, pc_geetest_key)
        challenge = request.POST.get(gt.FN_CHALLENGE, '')
        validate = request.POST.get(gt.FN_VALIDATE, '')
        seccode = request.POST.get(gt.FN_SECCODE, '')
        status = request.session[gt.GT_STATUS_SESSION_KEY]
        user_id = request.session["user_id"]
        if status:
            result = gt.success_validate(challenge, validate, seccode, user_id)
        else:
            result = gt.failback_validate(challenge, validate, seccode)
        if result:
            user = auth.authenticate(username=username, password=pwd)
            if user:
                auth.login(request, user)
                request.session['user']=username
                ret["msg"] = "/index/"
            else:
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误！"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"
        return JsonResponse(ret)
    return render(request, "login.html")


def upload(request):
    img=request.FILES.get('upload_img')
    path=os.path.join(settings.MEDIA_ROOT,'add_article_img',img.name)
    with open(path,'wb') as f:
        for line in img:
            f.write(line)
    ret={"error":0,
         "url":'/media/add_article_img/'+img.name}
    return HttpResponse(json.dumps(ret))

def addarticle(request):
    if request.method=='POST':
        user=request.user
        article_title=request.POST.get('title')
        article=request.POST.get('article')
        bs=BeautifulSoup(article, 'html.parser')
        article_context=bs.text
        article_desc=article_context[0:150]+'...'
        category=request.POST.get('category')
        tags=request.POST.getlist('tag')
        for tag in bs.find_all():
            if tag.name in ['script']:
                tag.decompose()
        detile=models.Detail.objects.create(detail=article)
        models.Article.objects.create(user=user,title=article_title,abstract=article_desc,detail=detile,category_id=category,)
        obj_article =models.Article.objects.filter(title=article_title)[0]
        for i in tags:
            obj_article.tag.add(i)

        return redirect('/index/')
    return render(request,'addarticle.html')


def comment(request):
    data={}
    user=request.user
    article=request.GET.get('article')
    context=request.GET.get('context')
    pid=request.GET.get('pid')
    if pid:
        models.Comments.objects.create(user=user,article_id=article,context=context,pid_id=pid)
    else:
        models.Comments.objects.create(user=user, article_id=article, context=context)
    comment_count=models.Comments.objects.filter(article_id=article).count()
    models.Article.objects.filter(nid=article).update(comment=comment_count)
    return JsonResponse(data)




def ud(request):
    data = {'state':0,'updown':0}
    user=request.user
    article=request.GET.get('article')
    updown=request.GET.get('updown')
    updown=json.loads(updown)

    try:
        models.Updown.objects.create(user=user,article=article,updown=updown)
        if updown:
            models.Article.objects.filter(pk=article).update(up=F("up")+1)
        else:
            models.Article.objects.filter(pk=article).update(down=F("down") + 1)
    except:
        updown2=models.Updown.objects.filter(user=user,article=article).first().updown
        if updown2==True:
            data={'state':1,'updown':1}
        else:
            data={'state':1,'updown':2}
    return JsonResponse(data)

def article_detile(request,username,article):
    comment_id=request.GET.get('comment_delete')
    if comment_id:
        models.Comments.objects.filter(nid=comment_id).delete()
    article = models.Article.objects.filter(nid=article)[0]
    ret = models.UserInfo.objects.filter(username=username)[0]
    comments=models.Comments.objects.filter(article=article)
    return render(request, 'article_detile.html', {'username':username, 'article': article,'ret':ret,'comments':comments})

def home(request,username):
    user=models.UserInfo.objects.filter(username=username).first()
    article=models.Article.objects.filter(user=user)
    return render(request,'home.html',{'username':username, 'article':article,'ret':user,})


def index(request):
    from mypage import Mypage
    page=request.GET.get('page')
    article=models.Article.objects.order_by("-up").all()
    category=request.GET.get('category')
    if category:
        article = models.Article.objects.filter(category=category).order_by("-up").all()
    mypage=Mypage(page,article,request.path,6)
    html=mypage.html
    ret=mypage.result
    category=models.Category.objects.all()
    return render(request,'index.html',{'article':ret,'html':html,'category':category})

def problem(request):
    if request.method=='POST':
        problem=request.POST.get('problem')
        models.Problem.objects.create(info=problem)
        return HttpResponse('提交成功')
    return render(request,'problem.html')

def userinfo(request):
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    if auth.authenticate(username=request.user,password=password):
        request.user.set_password(password2)
        request.user.save()
        return HttpResponse('修改成功')
    return render(request,'userinfo.html',)

def avater(request):
    head_photo=request.FILES.get('head_photo')
    user=models.UserInfo.objects.filter(username=request.user).first()
    user.avater=head_photo
    user.save()
    return render(request,'avater.html')