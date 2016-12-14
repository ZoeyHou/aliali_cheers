#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import User
from django.conf import settings
import base64

import face_recog as fr
import Transformation.process_img as p_i
import Transformation.get_filetype as ft


# 注册
def register(req):
    username = req.COOKIES.get("username", '')
    if req.method == "POST":
            print req
            username = req.POST.get('user', '')
            password = req.POST.get('password', '')
            avatar = req.FILES.get('avatar', '')
            discription = req.POST.get('discription', '')
            email = req.POST.get('email', '')
            filter_type = req.POST.get('filter_type', '')
            try:
            #将表单写入数据库
                user = User()
                user.username = username
                user.password = password
                if avatar and ft.get_pictype(avatar) in ft.image_type_tuple:
                    user.avatar = avatar
                else:
                    user.avatar = '/static/images/users/default_user.jpg'
                user.discription = discription
                user.email = email
                user.save()
                if filter_type != 'None' and avatar:
                    p_i.apply_filter(user, filter_type)
            except Exception, e:
                print Exception, ":", e
                return HttpResponse(e)

            response = HttpResponseRedirect('/login/recog_register/')
            response.set_cookie('username', username, 3600)
            return response

    return render_to_response("Authentication/signup.html", {'username':username,
                                                             'filter_list': p_i.filter_list})

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
        username = req.COOKIES.get("username", '')
        user = User.objects.filter(username=username)[0]

        img1 = req.POST.get('img1', '')
        img2 = req.POST.get('img2', '')
        img3 = req.POST.get('img3', '')
        img4 = req.POST.get('img4', '')
        img5 = req.POST.get('img5', '')

        face1 = open(settings.MEDIA_ROOT + "faces/" + username + "1.jpg", 'wb')
        face2 = open(settings.MEDIA_ROOT + "faces/" + username + "2.jpg", 'wb')
        face3 = open(settings.MEDIA_ROOT + "faces/" + username + "3.jpg", 'wb')
        face4 = open(settings.MEDIA_ROOT + "faces/" + username + "4.jpg", 'wb')
        face5 = open(settings.MEDIA_ROOT + "faces/" + username + "5.jpg", 'wb')

        face1.write(base64.b64decode(img1[23:]))
        face2.write(base64.b64decode(img2[23:]))
        face3.write(base64.b64decode(img3[23:]))
        face4.write(base64.b64decode(img4[23:]))
        face5.write(base64.b64decode(img5[23:]))

        face1.close()
        face2.close()
        face3.close()
        face4.close()
        face5.close()

        user.face1 = "faces/" + username + "1.jpg"
        user.face2 = "faces/" + username + "2.jpg"
        user.face3 = "faces/" + username + "3.jpg"
        user.face4 = "faces/" + username + "4.jpg"
        user.face5 = "faces/" + username + "5.jpg"
        user.save()

        fr.face_regist(user)

        return HttpResponse("Succ")
    else:
        username = req.COOKIES.get("username", '')
        if username:
            return render_to_response('Authentication/signup2.html', {"username": username})
        else:
            return HttpResponse("Not Login")

#人脸识别登录
def recog_login(req):
    if req.method == 'POST':
        img = req.POST['image'][23:]
        username = req.POST.get('username', '')
        imgData = base64.b64decode(img)

        #Debug code
        # with open('/home/william/test.jpg', 'w+') as im:
        #     im.write(imgData)


        user = User.objects.filter(username=username)
        if not user:
            return HttpResponse('User_not_exist')
        if fr.is_user(user[0].username, imgData):
            #用了ajax post,ajax请求无法重定向
            response = HttpResponse('T')
            response.set_cookie('username', username, 3600)
            return response
        else:
            return HttpResponse('F')


