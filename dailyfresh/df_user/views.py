# coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse
from hashlib import sha1

from models import *

# Create your views here.

def login(request):
    return render(request, 'df_user/login.html')

def login_handle(request):
    user_info = request.GET.get('user_info')
    User_info.objects.filter()

def register(request):
    context = {'title':'天天生鲜-注册'}
    return render(request, 'df_user/register.html', context)

def register_exist(request):
    user = request.GET.get('user_name')
    count = User_info.objects.filter(user_name=user).count()
    return JsonResponse({'count':count})

def register_handle(request):
    #{'user':user_name,'pwd':pwd,'cpwd':cpwd,'email':email,'allow':allow};
    #接收用户输入
    dict = request.POST
    user_name = dict.get('user_name')
    pwd = dict.get('pwd')
    cpwd = dict.get('cpwd')
    email = dict.get('email')
    #密码加密
    s1=sha1()
    s1.update(pwd)
    #创建对象
    user = User_info()
    user.user_name = user_name
    user.user_passwd = pwd
    user.user_mail = email
    user.save()
    #注册成功,返回登陆页面
    #ajax使用的是局部刷新,这里重定向的返回值并没有传递给浏览器,而是传递给ajax的function方法
    #return redirect('/user/login/')
    return JsonResponse({'redirect':'/user/login/'})







