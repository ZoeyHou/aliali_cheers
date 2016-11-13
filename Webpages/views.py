from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.conf import settings

from Authentication.models import User
from Webpages.models import Video

import json

def return_hello(req):
    username = req.COOKIES.get('username', '')
    return render(req, 'Webpages/hello.html', {'username': username})

def index(req):
    username = req.COOKIES.get('username', '')
    return render_to_response('Webpages/Home.html', {'username': username})

def gallery(req):
    username = req.COOKIES.get('username', '')
    user = User.objects.get(username=username)
    my_pic_list = user.User_Picture.all()
    return render_to_response('Webpages/Gallery.html', {'username': username, 'my_pic_list':my_pic_list})

def video(req):
    username = req.COOKIES.get('username', '')
    user = User.objects.get(username=username)
    my_video_list = user.User_Video.all()
    return render_to_response('Webpages/Video.html', {'username': username, 'my_video_list': my_video_list})

def playpage(req, video_name):
    username = req.COOKIES.get('username', '')
    return render_to_response('Webpages/play_page.html', {'username': username, 'video_name': video_name})

def barrage(req, video_name):
    username = req.COOKIES.get('username', '')
    ret = {}
    json_ret = ''
    ckplayer=[]
    time_spots=[]
    sentences=[]
    s = req.POST.get('s', '')
    j = req.POST.get('j', 0)

    v = Video.objects.get(video=video_name)
    vn=video_name.split('/')[1]
    if s:
        if not v.barrage:
            open(settings.MEDIA_ROOT + 'barrages/' + vn + '_' + 'barrage.json', 'w')
        barr_file = open(settings.MEDIA_ROOT + 'barrages/'+vn+'_'+'barrage.json', 'r+')
        barr_file.seek(0, 0)

        if v.barrage:
            content = barr_file.read()
            barr_file.seek(0, 0)
            print content
            ret = json.loads(content)
            ret['ckplayer'][0].append(j)
            ret['ckplayer'][1].append(s)
        else:
            temp2 = barr_file.name.split('/')[-1]
            temp1 = barr_file.name.split('/')[-2]
            v.barrage = temp1+'/'+temp2
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
        barr_file = open(settings.MEDIA_ROOT + 'barrages/'+vn+'_'+'barrage.json', 'rw')
        json_ret = barr_file.read()
        barr_file.close()

    return HttpResponse(json_ret)


