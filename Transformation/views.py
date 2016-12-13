# coding:utf-8
from Webpages.models import Picture, Video, Audio, Catagory
from Authentication.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from django.shortcuts import render_to_response
import os

import get_filetype as ft
import process_img as p_i
import process_video as p_v
import proccess_audio as p_a
import thumb

import threading


def upload_picture(req):
    if req.method == 'POST':
        pic = req.FILES.get('image')
        if pic and True:
            username = req.COOKIES.get('username', '')
            user = User.objects.get(username=username)
            picture = Picture(user=user, img=pic)
            picture.save()
            return HttpResponseRedirect('/gallery')
        else:
            return HttpResponse("要选择图片才能上传")
    else:
        return HttpResponseRedirect('/')


def upload_video(req):
    if req.method == 'POST':
        video = req.FILES.get('video')
        if video and True:
            username = req.COOKIES.get('username', '')
            user = User.objects.get(username=username)
            picture = Video(user=user, video=video)
            picture.save()
            return HttpResponseRedirect('/video')
        else:
            return HttpResponse("要选择视频才能上传")
    else:
        return HttpResponseRedirect('/')


def process_img(req):
    if req.method == 'POST':
        pic = req.FILES.get('image')
        if pic and True:
            username = req.COOKIES.get('username', '')
            user = User.objects.get(username=username)
            picture = Picture(user=user, img=pic)
            picture.save()
        else:
            return HttpResponse("要选择图片才能上传")

        (path_profix, file_name) = os.path.split(picture.img.path);
        (shotname, extension) = os.path.splitext(file_name);
        pro_file = ''

        if req.POST.get('file_type', ''):
            pro_file = 'pictures/' + shotname + '.' + req.POST['file_type']
            p_i.open_save(picture.img.path, settings.MEDIA_ROOT + pro_file)
        elif req.POST.get('display_mode', ''):
            pro_file = 'pictures/' + req.POST['display_mode'] + '_' + file_name
            p_i.mode_convert(picture.img.path, settings.MEDIA_ROOT + pro_file, req.POST['display_mode'])
        elif req.POST.get('set_filter', ''):
            pro_file = 'pictures/' + req.POST['set_filter'] + '_' + file_name
            p_i.set_filter(picture.img.path, settings.MEDIA_ROOT + pro_file, req.POST['set_filter'])
        elif req.POST.get('bsc_adjust', ''):
            pro_file = 'pictures/' + req.POST['bsc_adjust'] + '_' + file_name
            p_i.handle(picture.img.path, settings.MEDIA_ROOT + pro_file, req.POST['bsc_adjust'],
                       int(req.POST['adjust_value']))

        if pro_file:
            username = req.COOKIES.get('username', '')
            user = User.objects.get(username=username)
            picture1 = Picture(user=user, img=pro_file)
            picture1.save()

        return render_to_response('Transformation/transform_result.html', {'before': picture, 'after': picture1})


def process_video(req):
    if req.method == 'POST':
        video = req.FILES.get('video')
        target_fm = req.POST.get('format', '')
        target_ppi = req.POST.get('ppi', '')

        if video and True:
            username = req.COOKIES.get('username', '')
            user = User.objects.get(username=username)
            video_db = Video(user=user, video=video)
            video_db.save()
        else:
            return HttpResponse("要选择视频才能上传")

        video_name = str(video_db.video).split('/')[-1]
        if target_fm:
            t1 = threading.Thread(target=p_v.transform_format, args=(video_name, target_fm, user,))
        elif target_ppi:
            t1 = threading.Thread(target=p_v.transform_ppi, args=(video_name, target_ppi, user,))
        t1.setDaemon(True)
        t1.start()
        return HttpResponse("Processing...")


def upload(req):
    username = req.COOKIES.get("username", '')
    if username:
        catagory_list = Catagory.objects.all()
        if req.method == "POST":
            user = User.objects.get(username=username)
            file_type = req.POST.get("file_type", '')
            file = req.FILES.get("upload_file", '')
            catagory_name = req.POST.get("catagory", '')
            catagory = Catagory.objects.get(catagory_name=catagory_name)
            discription = req.POST.get("discription", '')
            title = req.POST.get("title", '')
            cover = req.FILES.get("discript_img", '')

            if file_type == "Video":
                if file:
                    v = Video(video=file, user=user, catagory=catagory,
                              discription=discription, title=title)
                    #这里调用是为了防止文件重名
                    v.save()
                    type = ft.get_videotype(v.video.path)
                    if type not in ft.video_type_tuple:
                        os.remove(v.video.path)
                        v.delete()
                        return HttpResponse("The formation is not supported!")
                    dir_path, file_name = os.path.split(v.video.path)
                    file_name = os.path.splitext(file_name)[0] + os.path.splitext(file_name)[1]

                    if not cover:
                        thumb.make_video_thumb(v.video.path, dir_path+"/cover/"+file_name+".jpg")
                    else:
                        thumb.make_thumb(cover, dir_path+"/cover/"+file_name+".jpg")

                    v.cover = "videos/cover/" + file_name + ".jpg"
                    v.save()

                    #转换低分辨率
                    t2 = threading.Thread(target=p_v.transform_ppi, args=(v,))
                    t2.setDaemon(True)
                    t2.start()
                    #转换格式
                    t1 = threading.Thread(target=p_v.transform_format, args=(v, ))
                    t1.setDaemon(True)
                    t1.start()

            elif file_type == "Audio":
                if file:
                    a = Audio(audio=file, user=user, catagory=catagory,
                              discription=discription, title=title)
                    a.save()

                    atype = ft.get_videotype(a.audio.path)
                    if atype not in ft.audio_type_tuple:
                        os.remove(a.audio.path)
                        a.delete()
                        return HttpResponse("The formation is not supported!")

                    dir_path, file_name = os.path.split(a.audio.path)
                    file_name = os.path.splitext(file_name)[0] + os.path.splitext(file_name)[1]
                    if not cover:
                        if thumb.get_audio_cover(file, dir_path+"/cover/"+file_name+".jpg"):
                            a.cover = "audios/cover/" + file_name + ".jpg"
                        else:
                            a.cover = '/static/images/audio/default_cover.jpg'
                    else:
                        thumb.make_thumb(cover, dir_path + "/cover/" + file_name + ".jpg")
                        a.cover = "audios/cover/" + file_name + ".jpg"
                    a.save()

                    t1 = threading.Thread(target=p_a.transform_format, args=(a, ))
                    t1.setDaemon(True)
                    t1.start()

            elif file_type == "Image":
                if file:
                    p = Picture(picture=file, user=user, catagory=catagory,
                                discription=discription, title=title)
                    p.save()

                    type = ft.get_pictype(p.picture.path)
                    #判断一下是不是我们要的类型
                    if type not in ft.image_type_tuple:
                        os.remove(p.picture.path)
                        p.delete()
                        return HttpResponse("The formation is not supported.")

                    dir_path, file_name = os.path.split(p.picture.path)
                    file_name = os.path.splitext(file_name)[0] + os.path.splitext(file_name)[1]
                    if not cover:
                        thumb.make_thumb(file, dir_path + "/cover/" + file_name + ".jpg")
                    else:
                        thumb.make_thumb(cover, dir_path + "/cover/" + file_name + ".jpg")
                    p.cover = "pictures/cover/" + file_name + ".jpg"
                    p.save()

                    t1 = threading.Thread(target=p_i.comlete_type, args=(p, type))
                    t1.setDaemon(True)
                    t1.start()

        return render_to_response("Transformation/upload.html", {'username': username,
                                                                 'catagory_list': catagory_list})
    else:
        return HttpResponse("Not_login")

