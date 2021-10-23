from django.shortcuts import render
from commodity.models import *
# Create your views here.
def indexVidew(request):
    title='首页'
    classContent=''
    commodityInfos=CommodityInfos.objects.order_by('-sold').all()[:3]

    #获取type表数据
    type_list=Types.objects.all()
    #type表里所有firsts是服饰的数据   ps:上衣,下衣
    f1=[x.seconds for x in type_list if x.firsts=='服饰']
    #comm表所有类型是f1  ps:所有类型是上衣,下衣
    clothes=CommodityInfos.objects.filter(types__in=f1).order_by('-sold')[:5]
    f2 = [x.seconds for x in type_list if x.firsts == '辅食']
    foods=CommodityInfos.objects.filter(types__in=f2).order_by('-sold')[:5]
    f3 = [x.seconds for x in type_list if x.firsts == '用品']
    goodss=CommodityInfos.objects.filter(types__in=f3).order_by('-sold')[:5]
    return render(request,'index.html',locals())