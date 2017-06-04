# coding=utf-8
from django.shortcuts import render
from models import *

# Create your views here.
def index(request):
    # 通过修改gtype_id查询
    # #获取商品对象列表,按点击次数由大->小进行排序
    # t_click = GoodsInfo.objects.filter(gtype_id=tid).order_by('-gclick')[0:3]
    # #获取商品对象列表,按上架时间由进->远进行排序
    # t_new = GoodsInfo.objects.filter(gtype_id=tid).order_by('-id')[0:4]
    # context = {'t1_click':t1_click, 't1_new':t1_new}

    #关联查询
    typelist = TypeInfo.objects.all()
    print typelist[0]
    type0 = typelist[0].goodsinfo_set.order_by('-gclick')[0:3]
    print type0
    t_clicklist = []
    t_newlist = []
    for item in range(0,6):
        t_clicklist.append(typelist[item].goodsinfo_set.order_by('-gclick')[0:3])
        t_newlist.append(typelist[item].goodsinfo_set.order_by('-id')[0:4])
    context = {
        'title':'首页','showcart':1,
        't_clicklist0':t_clicklist[0], 't_newlist0':t_newlist[0],
        't_clicklist1':t_clicklist[1], 't_newlist1':t_newlist[1],
        't_clicklist2':t_clicklist[2], 't_newlist2':t_newlist[2],
        't_clicklist3':t_clicklist[3], 't_newlist3':t_newlist[3],
        't_clicklist4':t_clicklist[4], 't_newlist4':t_newlist[4],
        't_clicklist5':t_clicklist[5], 't_newlist5':t_newlist[5],
    }

    return render(request, 'df_goods/index.html', context)

def list(request):
    return render(request, 'df_goods/list.html')

def detail(request):
    pass


