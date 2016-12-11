#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from django import forms
from django.conf import settings
import base64

import face_recog as fr


# 注册
def register(req):
    if req.method == "POST":
            print req
            username = req.POST.get('user', '')
            password = req.POST.get('password', '')
            avatar = req.FILES.get('avatar', '')
            discription = req.POST.get('discription', '')
            email = req.POST.get('email', '')
            try:
            #将表单写入数据库
                user = User()
                user.username = username
                user.password = password
                user.avatar = avatar
                user.discription = discription
                user.email = email
                user.save()
            except Exception, e:
                print Exception, ":", e
                return HttpResponse(e)

            response = HttpResponseRedirect('/login/recog_register/')
            response.set_cookie('username', username, 3600)
            return response

    return render_to_response("Authentication/signup.html")

#登录
def login(req):
    if req.method == 'POST':

        #获取表单用户密码
        username = req.POST.get('username', '')
        password = req.POST.get('password', '')
        #获取的表单数据与数据库进行比较
        user = User.objects.filter(username__exact=username, password__exact=password)
        if user:
            response = HttpResponse('T')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return HttpResponse('F')

def logout(req):
    response = HttpResponse('logout')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response


def recog_register(req):
    if req.method=='POST':
        img1 = req.POST.get('img1', '')
        img2 = req.POST.get('img2', '')
        img3 = req.POST.get('img3', '')
        username = req.COOKIES.get("username", '')
        user = User.objects.filter(username=username)[0]
        face1 = open(settings.MEDIA_ROOT+"faces/"+username+"1.jpg", 'wb')
        face2 = open(settings.MEDIA_ROOT + "faces/" + username + "2.jpg", 'wb')
        face3 = open(settings.MEDIA_ROOT + "faces/" + username + "3.jpg", 'wb')
        face1.write(base64.b64decode(img1[23:]))
        face2.write(base64.b64decode(img2[23:]))
        face3.write(base64.b64decode(img3[23:]))
        face1.close()
        face2.close()
        face3.close()
        user.face1 = "faces/"+username+"1.jpg"
        user.face2 = "faces/"+username+"2.jpg"
        user.face3 = "faces/"+username+"3.jpg"
        user.save()

        fr.face_regist(user)
    else:
        username = req.COOKIES.get("username", '')
        return render_to_response('Authentication/signup2.html', {"username": username})

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

