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

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #学习笔记主页

    #django 1.X版本里使用url模块，有3个实参，第一个实参是正则表达式，r让python将接下来的字符串视为原始字符串，^$代表表示正则的开始和末尾，
    #这个正则表达式让python查找开头和结尾没有任何东西的URL，此处与http://localhost:8000匹配
    #第二个实参指定了要调用的视图函数，第三个实参将这个URL模式的名称指定为index，使URL能够在其他地方引用

    #显示学习笔记主页面
    path('',views.index,name='index'),
    #显示主题页面
    path('topics/',views.topics,name='topics'),
    #用于显示特定主题的页面
    path('topics/(?P<topic_id>\d+)/',views.topic,name='topic'),
    #用于添加新主题的页面
    path('new_topic/',views.new_topic,name='new_topic'),
    #用于添加新条目的页面
    path('new_entry/(?P<topic_id>\d+)/',views.new_entry,name='new_entry'),
    #用于编辑条目的页面
    path('edit_entry/(?P<entry_id>\d+)/',views.edit_entry,name='edit_entry'),
]
