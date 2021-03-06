"""untitled6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings
from app01 import views
from app01 import urls as app01_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogregiste/', views.registe),
    url(r'^problem/', views.problem),

    url(r'^check_username/', views.check_username),
    url(r'^index/$', views.index),
    url(r'^pc-geetest/register/', views.get_geetest),
    url(r'^login/', views.login),
    url(r'^loginout/', views.loginout),
    url(r'^index/', include(app01_urls)),
    url(r'^ud/', views.ud),
    url(r'^comment/', views.comment),
    url(r'^userinfo/', views.userinfo),
    url(r'^avater/', views.avater),

    url(r'^addarticle/', views.addarticle),
    url(r'^upload/', views.upload),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
