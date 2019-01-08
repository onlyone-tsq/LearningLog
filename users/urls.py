#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-21 19:35:14
# @Author  : TSQ (812227146@qq.com)
# @Link    : ${link}
# @Version : $Id$

"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    #用户登陆页面

    #django 1.X版本里使用url模块，有3个实参，第一个实参是正则表达式，r让python将接下来的字符串视为原始字符串，^$代表表示正则的开始和末尾，
    #这个正则表达式让python查找开头和结尾没有任何东西的URL，此处与http://localhost:8000匹配
    #第二个实参指定了要调用的视图函数，第三个实参将这个URL模式的名称指定为index，使URL能够在其他地方引用

    #显示用户登陆主页面
    path('login/',LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register,name='register'),
]
