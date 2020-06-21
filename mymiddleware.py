from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render,HttpResponse,redirect


class myname(MiddlewareMixin):

    def process_request(self,request):
        path=['/login/','/pc-geetest/register/']
        if request.session.get('user') or request.path in path:
            return None
        return redirect('/login')

