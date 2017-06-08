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

def count_change(request):
    id = request.GET.get('id')
    count = request.GET.get('count')
    cart = CartInfo.objects.get(id=int(id))
    cart.count = int(count)
    cart.save()
    #　如果操作失败,返回数据库中count值
    return JsonResponse({'count': cart.count})

def list(request):
    cart_list = CartInfo.objects.filter(user_id=request.session['user_id'])
    context = {'title': '购物车','page_name': 1,
               'cart_list': cart_list,
               }
    return render(request, 'df_cart/cart.html',context)

def order(request):
    user = User_info.objects.get(id=request.session['user_id'])
    # 获取name='cart_id'可以获取他的value值
    # form 表单提交被勾选的部分
    cart_ids = request.GET.getlist('cart_id')
    carts_list = CartInfo.objects.filter(id__in=cart_ids)

    context = {'title':'订单页',
               'user_address':user.consignee_address,
               'user_name':user.consignee_name,
               'user_tel':user.consignee_tel,
               'carts_list':carts_list,
    }
    return render(request, 'df_order/place_order.html', context)