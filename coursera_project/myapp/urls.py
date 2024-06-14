from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns=[
    path('',views.test_form,name='form'),
    path('coursera/',views.coursera,name='coursera'),
    path('login/',LoginView.as_view(),name="login"),
]

