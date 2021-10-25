from django.urls import path
from .views import *
urlpatterns=[
        path('login',loginView,name='login'),
        path('logout',logoutView,name='logout'),
        path('',shopperView,name='shopper'),
        path('shoppercart',shoppercartView,name='shoppercart'),
        path('delete',deletAPI,name='delete'),
]