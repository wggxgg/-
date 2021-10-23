from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from  django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .form import *
from .models import *
# Create your views here.
def loginView(request):
    title='登录/注册'
    if request.method=='POST':
        infos=loginmodelform(data=request.POST)
        data=infos.data
        username=data['username']
        password=data['password']
        if User.objects.filter(username=username):
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect(reverse('shopper'))
            else:
                d=dict(username=username,password=password,is_active=1)
                user=User.objects.create_user(d)
                user.save()
                state='注册成功'
        else:
            error_msg=infos.errors.as_json()
            print(error_msg)
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
    try:
        paginator=paginator.page(p)
    except PageNotAnInteger:
        paginator=paginator.page(1)
    except EmptyPage:
        paginator=paginator.page(paginator.num_pages)
    return render(request,'shopper.html',locals())