from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from  django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import JsonResponse

from .form import *
from .models import *
from  commodity.models import *
# Create your views here.
def loginView(request):
    title='登录/注册'
    if request.method=='POST':
        infos=loginmodelform(data=request.POST)
        data=infos.data
        username=data['username']
        print(username)
        password=data['password']
        print(password)
        if User.objects.filter(username=username):
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(reverse('index'))
        else:
            d=dict(username=username,password=password,is_active=1)
            user=User.objects.create_user(**d)
            user.save()
            state='注册成功'
    else:
        infos=loginmodelform()
    return render(request,'login.html',locals())


@login_required(login_url='login')
def shopperView(request):
    title='个人中心'
    p=request.GET.get('p','1')
    t=request.GET.get('t','')
    paytime=request.session.get('paytime','')
    if t and paytime and t==paytime:
        payinfo=request.session.get('payinfo','')
        OrderInfos.objects.create(**payinfo)
        del request.session['paytime']
        del request.session['payinfo']
    orderinfos=OrderInfos.objects.filter(id=request.user.id).order_by('-created')
    paginator=Paginator(orderinfos,6)
    # print(paginator.object_list)
    try:
        paginator=paginator.page(p)
    except PageNotAnInteger:
        paginator=paginator.page(1)
    except EmptyPage:
        paginator=paginator.page(paginator.num_pages)
    return render(request,'shopper.html',locals())


def logoutView(request):
    logout(request)
    return redirect(reverse('shopper'))

@login_required(login_url='login')
def shoppercartView(request):
    title='我的购物车'
    classContent='shoppercart'
    id=request.GET.get('id','')
    quantity=request.GET.get('quantity',1)
    userID=request.user.id
    if id:
        CartInfos.objects.update_or_create(commodity_id=id,user_id=userID,quantity=quantity)
        return redirect(reverse('shoppercart'))
    getUserId=CartInfos.objects.filter(user_id=userID)
    commodityDcit={x.commodity_id:x.quantity for x in getUserId}
    commodityInfos=CommodityInfos.objects.filter(id__in=commodityDcit.keys())
    return render(request,'shopcart.html',locals())


def deletAPI(request):
    result={'state':'success'}
    userId=request.GET.get('usweId','')
    commodityid=request.GET.get('commodityid','')
    if userId:
        CartInfos.objects.filter(user_id=userId).delete()
    elif commodityid:
        CartInfos.objects.filter(commodity_id=commodityid).delete()
    else:
        result={'state':'fail'}
    return JsonResponse(result)