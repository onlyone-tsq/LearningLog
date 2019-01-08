# Create your views here.
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm

def logout_view(request):
    #注销用户
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    #注册新用户
    if request.method != 'POST':
        #显示新的注册表单，表单形式使用django自带的
        form = UserCreationForm()
    else:
        #处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #保存用户后，让用户自动登录，并重定向到学习笔记主页
            authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form':form}
    return render(request,'users/register.html',context)
