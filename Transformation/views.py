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
            filter_type = req.POST.get("filter_type", '')

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

                    if filter_type != 'None' and cover:
                        p_i.apply_filter(v, filter_type)

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

                    if filter_type != 'None' and cover:
                        p_i.apply_filter(a, filter_type)

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

                    if filter_type != 'None' and cover:
                        p_i.apply_filter(p, filter_type)

                    t1 = threading.Thread(target=p_i.comlete_type, args=(p, type))
                    t1.setDaemon(True)
                    t1.start()

        return render_to_response("Transformation/upload.html", {'username': username,
                                                                 'catagory_list': catagory_list,
                                                                 'filter_list': p_i.filter_list})
    else:
        return HttpResponse("Not_login")

