#coding:utf-8
from Webpages.models import Picture, Video
from Authentication.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings

from django.shortcuts import render_to_response
import os

import process_img as p_i
import process_video as p_v

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
            pro_file = 'pictures/'+shotname+'.'+req.POST['file_type']
            p_i.open_save(picture.img.path, settings.MEDIA_ROOT+pro_file)
        elif req.POST.get('display_mode', ''):
            pro_file = 'pictures/'+req.POST['display_mode']+'_'+file_name
            p_i.mode_convert(picture.img.path, settings.MEDIA_ROOT+pro_file, req.POST['display_mode'])
        elif req.POST.get('set_filter', ''):
            pro_file = 'pictures/'+req.POST['set_filter']+'_'+file_name
            p_i.set_filter(picture.img.path, settings.MEDIA_ROOT+pro_file, req.POST['set_filter'])
        elif req.POST.get('bsc_adjust', ''):
            pro_file = 'pictures/'+req.POST['bsc_adjust']+'_'+file_name
            p_i.handle(picture.img.path, settings.MEDIA_ROOT+pro_file, req.POST['bsc_adjust'], int(req.POST['adjust_value']))

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


