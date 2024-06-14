from django.urls import path
from . import views

app_name='question'

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login,name='login'),
    path('logout',views.Logout,name='logout'),
    path('start',views.index,name='index'),
    path('result/',views.check_result,name='result'),
    path('add-question/',views.add_question,name='add_question'),
    path('add-choice/',views.add_choice,name='add_choice'),
    path('add-answer/',views.add_answer,name='add_answer'),
]