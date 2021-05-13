from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name = 'home'),
    path('add', views.add, name = 'add'),
    path('result', views.result, name = 'result'),
    path('new', views.new, name = 'new'),
    path('mark', views.mark, name = 'mark'),
    path('changeMark', views.changeMark, name= 'changeMark'),
    path('back', views.home, name= 'home'),
]