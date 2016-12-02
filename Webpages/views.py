# coding:utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q

from Authentication.models import User
from Webpages.models import Video, Audio, Picture
from Webpages.models import Like_Item, Dislike_Item, Collect_Item
from Webpages.models import Catagory

import json


def return_hello(req):
    username = req.COOKIES.get('username', '')
    return render(req, 'Webpages/hello.html', {'username': username})


def index(req):
    username = req.COOKIES.get('username', '')
    video_list = Video.objects.all()[:8]
    audio_list = Audio.objects.all()[:8]
    picture_list = Picture.objects.all()[:8]
    return render_to_response('Webpages/index.html', {'username': username,
                                                      "video_list": video_list,
                                                      'audio_list': audio_list,
                                                      'picture_list': picture_list})


# 个人主页，对应url /personal_page
def personal_page(req, page_username):
    username = req.COOKIES.get("username", '')
    page_user = User.objects.get(username=page_username)
    video_list = Video.objects.filter(user__username=page_username)[:5]
    audio_list = Audio.objects.filter(user__username=page_username)[:5]
    image_list = Picture.objects.filter(user__username=page_username)[:5]
    if username:
        return render_to_response('Webpages/personal_page.html', {'username': username,
                                                                  'page_user': page_user,
                                                                  'video_list': video_list,
                                                                  'audio_list': audio_list,
                                                                  'image_list': image_list})
    else:
        return HttpResponse("Not_login")


def edit_info(req):
    username = req.COOKIES.get("username", '')
    if username:
        user = User.objects.get(username=username)

    if req.method == "POST":
        pass
    else:
        return render_to_response("Webpages/edit.html", {"username": username, "user": user})


def more_upload(req, page_username, type):
    username = req.COOKIES.get("username", '')
    if type == "video" or type == "video/":
        vlist = Video.objects.filter(user__username=page_username)
        return render_to_response("Webpages/uploaded_video.html", {'list': vlist,
                                                                   'username': username})
    elif type == "audio" or type == "audio/":
        alist = Audio.objects.filter(user__username=page_username)
        return render_to_response("Webpages/uploaded_audio.html", {'list': alist,
                                                                   'username': username})
    elif type == "picture" or type == "picture/":
        plist = Picture.objects.filter(user__username=page_username)
        return render_to_response("Webpages/uploaded_image.html", {'list': plist,
                                                                   'username': username})


def search(req):
    username = req.COOKIES.get("username", '')
    if req.method == "POST":
        pass
    return render_to_response("Webpages/search.html", {"username": username})


# audio展示页面，对应url /audio
def audio(req):
    username = req.COOKIES.get('username', '')

    catagories = Catagory.objects.all()[:8]
    audio_list = {}
    for i in range(len(catagories)):
        audio_list[catagories[i].catagory_name] = Audio.objects.filter(catagory=catagories[i])[:8]

    return render_to_response('Webpages/audio.html', {'username': username,
                                                      'audio_list': audio_list})


def audio_playpage(req, audio_name):
    username = req.COOKIES.get('username', '')
    audio = Audio.objects.filter(audio=audio_name)[0]
    comments = audio.Audio_Comment.all()
    return render_to_response('Webpages/audio_display.html',
                              {'username': username, 'audio': audio, 'comments': comments})


def audio_lyric(req, audio_name):
    return render_to_response('Webpages/lyric.html')


# photo展示页面，对应url /gallery
def gallery(req):
    username = req.COOKIES.get('username', '')
    catagories = Catagory.objects.all()[:8]
    picture_list = {}
    for i in range(len(catagories)):
        picture_list[catagories[i].catagory_name] = Picture.objects.filter(catagory=catagories[i])[:8]

    return render_to_response('Webpages/image.html', {'username': username,
                                                      "picture_list": picture_list})


def picture_display(req, pic_name):
    username = req.COOKIES.get("username", '')
    picture = Picture.objects.filter(picture=pic_name)[0]
    comments = picture.Picture_Comment.all()

    return render_to_response("Webpages/image_display.html", {"username": username,
                                                              "picture": picture,
                                                              "comments": comments})


# video展示页面，对应url /video
def video(req):
    username = req.COOKIES.get('username', '')

    catagories = Catagory.objects.all()[:8]
    video_list = {}
    for i in range(len(catagories)):
        video_list[catagories[i].catagory_name] = Video.objects.filter(catagory=catagories[i])[:8]

    return render_to_response('Webpages/video.html', {'video_list': video_list,
                                                      'username': username})


# 播放页面 对应url playpage/(.+)/
def playpage(req, video_name):
    username = req.COOKIES.get('username', '')
    v = Video.objects.filter(video=video_name)[0]
    comments = v.Video_Comment.all()
    recommand_list = Video.objects.filter(~Q(video=v.video) & Q(catagory=v.catagory))[:5]
    if username:
        user = User.objects.get(username=username)
        return render_to_response('Webpages/video_display.html',
                                  {'username': username, 'carrent_user': user,
                                   'video': v, 'comments': comments, "recommand_list": recommand_list})
    return render_to_response('Webpages/video_display.html',
                              {'username': username, 'video': v, 'comments': comments,
                               "recommand_list": recommand_list})


# 响应弹幕请求的函数，对应url /playpage/(.+)/barrage$
def barrage(req, video_name):
    ret = {}
    json_ret = ''
    ckplayer = []
    time_spots = []
    sentences = []
    s = req.POST.get('s', '')
    j = req.POST.get('j', 0)

    v = Video.objects.get(video=video_name)
    vn = video_name.split('/')[1]
    if s:
        if not v.barrage:
            open(settings.MEDIA_ROOT + 'barrages/' + vn + '_' + 'barrage.json', 'w')
        barr_file = open(settings.MEDIA_ROOT + 'barrages/' + vn + '_' + 'barrage.json', 'r+')
        barr_file.seek(0, 0)

        if v.barrage:
            content = barr_file.read()
            barr_file.seek(0, 0)
            ret = json.loads(content)
            ret['ckplayer'][0].append(j)
            ret['ckplayer'][1].append(s)
        else:
            temp2 = barr_file.name.split('/')[-1]
            temp1 = barr_file.name.split('/')[-2]
            v.barrage = temp1 + '/' + temp2
            v.save()
            time_spots.append(j)
            sentences.append(s)
            ckplayer.append(time_spots)
            ckplayer.append(sentences)
            ret['ckplayer'] = ckplayer

        json_ret = json.dumps(ret)
        barr_file.write(json_ret)
        barr_file.close()

    elif v.barrage:
        barr_file = open(settings.MEDIA_ROOT + 'barrages/' + vn + '_' + 'barrage.json', 'rw')
        json_ret = barr_file.read()
        barr_file.close()

    return HttpResponse(json_ret)


def like_and_collect(req):
    username = req.COOKIES.get("username", '')

    if req.method == "POST" and username:
        user = User.objects.get(username=username)
        req_type = req.POST['type']

        if req_type == 'video_like':
            vn = req.POST['video_name']
            v = Video.objects.get(video=vn)
            if not Like_Item.objects.filter(user=user, video=v):
                v.like += 1
                v.save()
                LikeItem = Like_Item(user=user, video=v)
                LikeItem.save()
                return HttpResponse("T")
            else:
                return HttpResponse("F")

        elif req_type == 'video_dislike':
            vn = req.POST['video_name']
            v = Video.objects.get(video=vn)
            if not Dislike_Item.objects.filter(user=user, video=v):
                v.dislike += 1
                v.save()
                DislikeItem = Dislike_Item(user=user, video=v)
                DislikeItem.save()
                return HttpResponse("T")
            else:
                return HttpResponse("F")

        elif req_type == "video_collect":
            vn = req.POST['video_name']
            v = Video.objects.get(video=vn)
            if not Collect_Item.objects.filter(user=user, video=v):
                v.save()
                CollectItem = Collect_Item(user=user, video=v)
                CollectItem.save()
                return HttpResponse("T")
            else:
                return HttpResponse("F")


def about_us(req):
    username = req.COOKIES.get("username", '')
    return render_to_response('Webpages/about.html', {'username': username})
