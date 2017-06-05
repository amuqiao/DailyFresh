# coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render

from models import *
from django.core.paginator import Paginator

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
#传入三个参数：分类 页码　排序类型
def list(request, tid, pindex, orderby):

    #根据tid查询所有商品信息->根据order进行排序->根据pindex显示第几页
    #根据传入的pid查询商品类型
    gtype = TypeInfo.objects.get(id = tid)
    #查询最新两条商品信息 一对多查询
    new_list = gtype.goodsinfo_set.order_by('-id')[0:2]
    #查询该类型所有商品
    #goods_list = gtype.goodsinfo_set.all()
    goods_list = GoodsInfo.objects.filter(gtype_id = int(tid))
    #排序  默认(上架时间)　价格　人气　
    if orderby == '1':
        goods_list = goods_list.order_by('-id')
    elif orderby == '2':
        goods_list = goods_list.order_by('-gprice')
    elif orderby == '3':
        goods_list = goods_list.order_by('-gclick')

    # 分页->显示  每页10条数据
    paginator = Paginator(goods_list, 3)
    pindex2 = int(pindex)
    # 对页码范围进行限制
    if pindex2 <= 0:
        pindex2 = 1
    elif pindex2 >= paginator.num_pages:
        pindex2 = paginator.num_pages

    # 显示当前页面所有数据
    page = paginator.page(pindex2)

    # 构造上下文
    context = {'title':'列表页', 'page':page,
        'tid':tid, 'gtype':gtype,
        'orderby':orderby, 'new_list':new_list,
    }
    return render(request, 'df_goods/list.html', context)
def detail(request):
    pass




