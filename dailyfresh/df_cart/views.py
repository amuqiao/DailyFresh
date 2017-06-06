# coding=utf-8

from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from models import *

# Create your views here.

def add(request, gid, count):
    # ［objects,］没查到则返回空列表
    carts = CartInfo.objects.filter(goods_id=gid).filter(user_id=request.session['user_id'])
    if len(carts) == 0:
        cart = CartInfo()
        cart.goods_id = int(gid)
        cart.user_id = request.session['user_id']
        cart.count = int(count)
        cart.save()
    else:
        cart = carts[0]
        cart.count += int(count)
        cart.save()

    # list通过request提交数据,返回response对象进行页面刷新
    # detail通过ajax提交数据,只能接收JsonResponse对象
    if request.is_ajax():
        # count为购物车中商品的数量
        return JsonResponse({'count':CartInfo.objects.filter(user_id=request.session['user_id']).count()})
    else:
        return redirect('/cart/')

def list(request):
    context = {'title':'购物车',
               }
    return render(request, 'df_cart/cart.html',context)
