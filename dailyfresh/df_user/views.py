# coding=utf-8
from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from hashlib import sha1

from models import *

# Create your views here.

def login(request):
    return render(request, 'df_user/login.html')

def login_handle(request):
    #　接收请求信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    jizhu = post.get('jizhu', 0)
    #　根据用户名查询对象
    users = User_info.objects.filter(user_name=uname)
    print users
    #　判断１.未查到则用户名错　２.查询到　则判断密码是否正确, 正确则转到用户中心
    if len(users)==1:
        s1 = sha1()
        s1.update(upwd)
        print s1.hexdigest()
        print users[0].user_passwd
        # 　查询集第一条数据upwd属性
        if s1.hexdigest()==users[0].user_passwd:

            #读取cookies中设置的url为根目录
            #这句话怎么理解?读取cookies,没有读取到则设置一个默认值？
            url = request.COOKIES.get('url','/')
            print url
            red = HttpResponseRedirect(url)
            # 成功后删除转向地址，防止以后直接登录造成的转向
            # 为什么要删除?
            red.set_cookie('url','',max_age=-1)

            #记住用户名
            if jizhu!=0:
                red.set_cookie('uname', uname)
            else:
                red.set_cookie('uname','',max_age=-1)
            # 记住用户名为什么不直接存session,反而要先存cookies?
            request.session['user_id']=users[0].id
            request.session['user_name']=uname
            return red
        else:
            context = {'title':'用户登陆','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录','error_name':1,'error_pwd': 0,'uname':uname,'upwd':upwd}
        return render(request,'df_user/login.html',context)









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
    pwd2 = s1.hexdigest()

    #创建对象
    user = User_info()
    user.user_name = user_name
    user.user_passwd = pwd2
    user.user_mail = email
    user.save()
    #注册成功,返回登陆页面
    #ajax使用的是局部刷新,这里重定向的返回值并没有传递给浏览器,而是传递给ajax的function方法
    #return redirect('/user/login/')
    return JsonResponse({'redirect':'/user/login/'})







