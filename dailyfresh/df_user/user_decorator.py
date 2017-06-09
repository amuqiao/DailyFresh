# coding=utf-8
from django.shortcuts import redirect
from django.http import JsonResponse


#　如果未登陆则转到登陆页面
def login(func):
    def login_inner(request, *args, **kwargs):
        if request.session.has_key('user_id'):
            return func(request, *args, **kwargs)
        else:
            if request.is_ajax():
                return JsonResponse({'islogin':0})
            else:
                return redirect('/user/login/')
    return login_inner





