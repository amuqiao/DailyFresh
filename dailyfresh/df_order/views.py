# coding=utf-8
from django.shortcuts import render
from df_user.models import *
from df_goods.models import *
from df_cart.models import *


# Create your views here.

def order(request):
    user = User_info.objects.get(id=request.session['user_id'])
    carts_list = CartInfo.objects.filter(user_id=request.session['user_id'])

    context = {'title':'订单页',
               'user_address':user.consignee_address,
               'user_name':user.consignee_name,
               'user_tel':user.consignee_tel,
               'carts_list':carts_list,
    }
    return render(request, 'df_order/place_order.html', context)