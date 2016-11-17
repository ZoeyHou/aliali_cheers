#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from django import forms
import base64

import face_recog as fr


#定义表单模型
class UserForm(forms.Form):
    username = forms.CharField(label='用户名：',max_length=100)
    password = forms.CharField(label='密码：',widget=forms.PasswordInput())

# 注册
def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            user.save()
            #返回注册成功页面
            return render_to_response('Authentication/success.html', {'username': username})
    else:
        uf = UserForm()
    return render_to_response('Authentication/register.html', {'uf': uf})

#登录
def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                response = HttpResponseRedirect('/')
                response.set_cookie('username', username, 3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('Authentication/login.html',{'uf':uf})

def logout(req):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response


def recog_register(req):
    username = req.COOKIES.get("username", '')
    fr.face_regist(User.objects.filter(username=username)[0])

#人脸识别登录
def recog_login(req):
    if req.method == 'POST':
        img = req.POST['image'][23:]
        username = req.POST.get('username', '')
        imgData = base64.b64decode(img)

        user = User.objects.filter(username=username)[0]
        if fr.is_user(user.username, imgData):
            #用了ajax post,ajax请求无法重定向
            response = HttpResponse('T')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return HttpResponse('F')

    return render_to_response('Authentication/recog_login.html')