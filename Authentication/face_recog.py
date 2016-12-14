# coding: utf-8
from django.conf import settings

import requests
import os
import time
from pprint import pformat

from faceAPI_init import API_KEY, API_SECRET, api


def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj

    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width=75).split('\n')])


def get_local_faceid(imgData):
    # 目前的API网址是这个，在API文档里找
    BASE_URL = 'http://apicn.faceplusplus.com/v2'

    # 使用Requests上传图片
    url = '%s/detection/detect?api_key=%s&api_secret=%s&attribute=none' % (BASE_URL, API_KEY, API_SECRET)
    files = {'img': ("user.jpg", imgData, "jpg")}

    r = requests.post(url, files=files)

    # 如果读取到图片中的头像则输出，其中的'face_id'就是所需值
    faces = r.json().get('face')
    face_id = 0
    print faces
    if faces:
        face_id = faces[0]['face_id']
        # print face_id

    return face_id


def verify_face(name, face_id):
    result = api.recognition.verify(person_name=name, face_id=face_id)
    print '=' * 60
    print_result('Recognize result:', result)
    print '=' * 60
    if result['is_same_person']:
        print 'It is the same person'
        return True
    return False


def delete_pergro(name, group):
    api.group.delete(group_name=group)
    api.person.delete(person_name=name)
    print 'delete done!'


# name为人的姓名， group为组名， face_list为预设人的三张图片
def create_person(name, group, face_list):
    face_id = get_local_faceid(open(face_list[0][1], 'rb'))
    try:
        api.person.create(person_name=name, group_name=group,
                          face_id=face_id)
    except Exception:
        print 'Person has created'
    print 'person create done'

    for i in range(1, len(face_list)):
        face_id = get_local_faceid(open(face_list[0][1], 'rb'))
        api.person.add_face(person_name=name, face_id=face_id)
        print 'add %d' % i
    print 'add all done'


# name为人名
def train_person(name):
    result = api.train.verify(person_name=name)
    print_result('Train result:', result)
    session_id = result['session_id']

    while True:
        result = api.info.get_session(session_id=session_id)
        if result['status'] == u'SUCC':
            print_result('Async train result:', result)
            break
        time.sleep(1)
    print 'train done'


def face_regist(user):
    # 根据人和组进行命名修改
    NAME = user.username
    GROUP = 'test'

    # 预设的三张图片，名字和文件位置
    face_list = [(NAME, settings.MEDIA_ROOT + str(user.face1)),
                 (NAME, settings.MEDIA_ROOT + str(user.face2)),
                 (NAME, settings.MEDIA_ROOT + str(user.face3)),
                 (NAME, settings.MEDIA_ROOT + str(user.face3)),
                 (NAME, settings.MEDIA_ROOT + str(user.face3)),]
    create_person(name=NAME, group=GROUP, face_list=face_list)
    train_person(name=NAME)


def is_user(username, img):
    target_face = img
    target_face_id = get_local_faceid(target_face)
    final_result = False
    print 'target face id done : %s' % target_face_id
    if target_face_id:
        final_result = verify_face(username, target_face_id)

    return final_result
