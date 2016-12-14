# coding:utf-8

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.db.models import Q

from Authentication.models import User
from Webpages.models import Video, Audio, Picture
from Webpages.models import Like_Item, Dislike_Item, Collect_Item
from Webpages.models import Video_Comment, Audio_Comment, Picture_Comment
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
    collect_video_list = page_user.Collect_User.filter(~Q(video=None))[:5]
    collect_audio_list = page_user.Collect_User.filter(~Q(audio=None))[:5]
    collect_image_list = page_user.Collect_User.filter(~Q(picture=None))[:5]
    if username:
        return render_to_response('Webpages/personal_page.html', {'username': username,
                                                                  'page_user': page_user,
                                                                  'video_list': video_list,
                                                                  'audio_list': audio_list,
                                                                  'image_list': image_list,
                                                                  "collect_video_list": collect_video_list,
                                                                  "collect_audio_list": collect_audio_list,
                                                                  "collect_image_list": collect_image_list,})
    else:
        return HttpResponse("Not_login")


def edit_info(req):
    username = req.COOKIES.get("username", '')
    if username:
        user = User.objects.get(username=username)

    if req.method == "POST":
        discription = req.POST.get('discription', '')
        avatar = req.FILES.get("avatar", '')
        user.discription = discription
        if avatar:
            user.avatar = avatar
        user.save()
        return HttpResponseRedirect("/personal_page/"+username+'/')

    else:
        return render_to_response("Webpages/edit.html", {"username": username, "user": user})


def more_upload(req, page_username, type):
    username = req.COOKIES.get("username", '')
    page_user = User.objects.get(username=page_username)
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
    elif type == "video_collected" or type == "video_collected/":
        vclist = page_user.Collect_User.filter(~Q(video=None))
        return render_to_response("Webpages/collected_video.html", {'list': vclist,
                                                                   'username': username})
    elif type == "audio_collected" or type == "audio_collected/":
        aclist = page_user.Collect_User.filter(~Q(audio=None))
        return render_to_response("Webpages/collected_audio.html", {'list': aclist,
                                                                   'username': username})
    elif type == "picture_collected" or type == "picture_collected/":
        pclist = page_user.Collect_User.filter(~Q(picture=None))
        return render_to_response("Webpages/collected_image.html", {'list': pclist,
                                                                   'username': username})



def search(req):
    username = req.COOKIES.get("username", '')
    catagory_items = Catagory.objects.all()
    if req.method == 'POST':
        search_input = req.POST.get('search_input', '')
        catagories = req.POST.get('catagory', '')

        if search_input and catagories:
            catagories_list = catagories.split(',')
            my_filter_qs = Q()
            for c_item in catagories_list[:-1]:
                my_filter_qs = (my_filter_qs | Q(catagory__catagory_name=c_item))
            my_filter_qs = (my_filter_qs & Q(title__contains=search_input))

            audio_list = Audio.objects.filter(my_filter_qs)[:40]
            video_list = Video.objects.filter(my_filter_qs)[:40]
            picture_list = Picture.objects.filter(my_filter_qs)[:40]
            user_list = User.objects.filter(username=search_input)[:40]
            return render_to_response("Webpages/search.html", {"username": username,
                                                           "catagories": catagory_items,
                                                           "audio_list": audio_list,
                                                            "video_list": video_list,
                                                            "picture_list": picture_list,
                                                            "user_list": user_list, })
        elif search_input and not catagories:
            user_list = User.objects.filter(username=search_input)[:40]
            return render_to_response("Webpages/search.html", {"username": username,
                                                               "catagories": catagory_items,
                                                               "user_list": user_list, })

    return render_to_response("Webpages/search.html", {"username": username, "catagories": catagory_items})


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
    recommand_list = Audio.objects.filter(~Q(audio=audio.audio) & Q(catagory=audio.catagory))[:5]
    if username:
        user = User.objects.get(username=username)
        return render_to_response('Webpages/audio_display.html',
                                  {'username': username, 'current_user': user,
                                   "audio": audio, 'comments': comments, "recommand_list": recommand_list})
    return render_to_response('Webpages/audio_display.html',
                              {'username': username, "audio": audio, 'comments': comments,
                               "recommand_list": recommand_list})


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
    recommand_list = Picture.objects.filter(~Q(picture=picture.picture) & Q(catagory=picture.catagory))[:5]
    if username:
        user = User.objects.get(username=username)
        return render_to_response('Webpages/image_display.html',
                                  {'username': username, 'current_user': user,
                                   "picture": picture, 'comments': comments, "recommand_list": recommand_list})
    return render_to_response('Webpages/image_display.html',
                              {'username': username, "picture": picture, 'comments': comments,
                               "recommand_list": recommand_list})



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
                                  {'username': username, 'current_user': user,
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
        m_type = req.POST['mtype']

        if req_type == 'like':
            if m_type == 'video':
                vn = req.POST['video_name']
                v = Video.objects.get(video=vn)
                if not (Like_Item.objects.filter(user=user, video=v)\
                        or Dislike_Item.objects.filter(user=user, video=v)):
                    v.like += 1
                    v.save()
                    LikeItem = Like_Item(user=user, video=v)
                    LikeItem.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")
            elif m_type == 'audio':
                an = req.POST['audio_name']
                a = Audio.objects.get(audio=an)
                if not (Like_Item.objects.filter(user=user, audio=a)\
                        or Dislike_Item.objects.filter(user=user, audio=a)):
                    a.like += 1
                    a.save()
                    LikeItem = Like_Item(user=user, audio=a)
                    LikeItem.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")
            elif m_type == 'image':
                pn = req.POST['image_name']
                p = Picture.objects.get(picture=pn)
                if not (Like_Item.objects.filter(user=user, picture=p)\
                        or Dislike_Item.objects.filter(user=user, picture=p)):
                    p.like += 1
                    p.save()
                    LikeItem = Like_Item(user=user, picture=p)
                    LikeItem.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")

        elif req_type == 'dislike':
            if m_type == 'video':
                vn = req.POST['video_name']
                v = Video.objects.get(video=vn)
                if not (Dislike_Item.objects.filter(user=user, video=v)\
                        or Like_Item.objects.filter(user=user, video=v)):
                    v.dislike += 1
                    v.save()
                    DislikeItem = Dislike_Item(user=user, video=v)
                    DislikeItem.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")
            elif m_type == 'audio':
                an = req.POST['audio_name']
                a = Audio.objects.get(audio=an)
                if not (Dislike_Item.objects.filter(user=user, audio=a)\
                        or Like_Item.objects.filter(user=user, audio=a)):
                    a.dislike += 1
                    a.save()
                    DislikeItem = Dislike_Item(user=user, audio=a)
                    DislikeItem.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")
            elif m_type == 'image':
                pn = req.POST['image_name']
                p = Picture.objects.get(picture=pn)
                if not (Dislike_Item.objects.filter(user=user, picture=p)\
                        or Like_Item.objects.filter(user=user, picture=p)):
                    p.dislike += 1
                    p.save()
                    DislikeItem = Dislike_Item(user=user, picture=p)
                    DislikeItem.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")

        elif req_type == "collect":
            if m_type == "video":
                vn = req.POST['video_name']
                v = Video.objects.get(video=vn)
                if not Collect_Item.objects.filter(user=user, video=v):
                    v.save()
                    CollectItem = Collect_Item(user=user, video=v)
                    CollectItem.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")
            elif m_type == "audio":
                an = req.POST['audio_name']
                a = Audio.objects.get(audio=an)
                if not Collect_Item.objects.filter(user=user, audio=a):
                    CollectItem = Collect_Item(user=user, audio=a)
                    CollectItem.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")
            elif m_type == "image":
                pn = req.POST['image_name']
                p = Picture.objects.get(picture=pn)
                if not Collect_Item.objects.filter(user=user, picture=p):
                    p.save()
                    CollectItem = Collect_Item(user=user, picture=p)
                    CollectItem.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")

        elif req_type == "comment":
            if m_type == "video":
                vn = req.POST['video_name']
                c = req.POST.get("comment_input")
                if c != '':
                    v = Video.objects.get(video=vn)
                    u = User.objects.get(username=username)
                    vcom = Video_Comment(video=v, user=u, content=c)
                    vcom.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")
            elif m_type == "audio":
                an = req.POST['audio_name']
                c = req.POST.get("comment_input")
                if c != '':
                    a = Audio.objects.get(audio=an)
                    u = User.objects.get(username=username)
                    acom = Audio_Comment(audio=a, user=u, content=c)
                    acom.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")
            elif m_type == "image":
                pn = req.POST['image_name']
                c = req.POST.get("comment_input")
                if c != '':
                    p = Picture.objects.get(picture=pn)
                    u = User.objects.get(username=username)
                    pcom = Picture_Comment(picture=p, user=u, content=c)
                    pcom.save()
                    return HttpResponse("T")
                else:
                    return HttpResponse("F")



def about_us(req):
    username = req.COOKIES.get("username", '')
    return render_to_response('Webpages/about.html', {'username': username})
