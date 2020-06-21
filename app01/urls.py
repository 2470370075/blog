from django.conf.urls import url
from app01 import views

urlpatterns = [

    url(r'^(\w+)/(\d+)', views.article_detile),
    url(r'^(\w+)/$',views.home),

]
