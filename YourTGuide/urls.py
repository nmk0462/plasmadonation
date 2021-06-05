from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("login",views.login_view,name="login"),
    path("register",views.register,name="register"),
    path("logout",views.logout_view,name="logout"),
    path("donate",views.donate,name="donate"),
    path("sub",views.sub,name="sub"),
    path("search",views.search,name="search"),
    path("find",views.find,name="find"),
    path("req",views.req,name="req"),
    path("help",views.hlp,name="hlp"),
    path("dels",views.dels,name="dels"),
    path("del1/<str:mn>",views.del1,name="del1"),
    path("del2/<str:mn1>",views.del2,name="del2"),
    path("next",views.next,name="next"),
    path("info",views.info,name="info"),
    path("chk/<str:ppn>",views.chk,name="chk"),
    path("ffo",views.ffo,name="ffo")
]