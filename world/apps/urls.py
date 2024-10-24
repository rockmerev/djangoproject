from django.urls import path,include
from . import views
urlpatterns=[
    path("home",views.home),
    path("tq",views.tq),
    path("signup",views.signupp),
    path("login",views.login)
]