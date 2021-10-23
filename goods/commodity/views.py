from django.shortcuts import render
from commodity.models import *
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def commondityView(request):
    title='商品列表'
    classContent='commoditys'

    #页数
    p=request.GET.get('p','1')
    #排序
    s=request.GET.get('s','sold')
    #关键字
    n=request.GET.get('n','')
    #分类
    t=request.GET.get('t','')

    #一级目录
    firsts=Types.objects.values('firsts').distinct()
    typeslist=Types.objects.all()

    commodityinfos=CommodityInfos.objects.all()
    if s:
        commodityinfos=commodityinfos.order_by('-'+s)
    elif n:
        commodityinfos=commodityinfos.filter(name__contains=n).all()
    elif t:
        types=Types.objects.filter(id=t).first()
        commodityinfos=commodityinfos.filter(types=types.seconds).all()

    paginator=Paginator(commodityinfos,6)

    try:
        paginator=paginator.page(p)
    except EmptyPage:
        paginator=paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        paginator=paginator.page(1)
    return render(request,'commodity.html',locals())


def detailView(request,id):
    title='商品介绍'
    classContent='datails'
    commo=CommodityInfos.objects.filter(id=id).first()
    items=CommodityInfos.objects.exclude(id=id).order_by('-sold')[:5]
    likelist=request.session.get('linkes',[])
    likes=True if id in likelist else False
    return render(request,'details.html',locals())