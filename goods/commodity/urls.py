from django.urls import path
from . import views


urlpatterns=[
    path('.html',views.commondityView,name='commondity'),
    path('/detail.<int:id>.hmtl',views.detailView,name='detail'),
]