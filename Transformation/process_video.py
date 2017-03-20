# -*- coding: UTF-8 -*-

import os
from os.path import join
from django.conf import settings

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

source_path = settings.MEDIA_ROOT + 'videos'
out_path = settings.MEDIA_ROOT + 'videos'

def transform_format(v):
    f = str(v.video).split('/')[-1].split('.')
    file_name = f[:-1]
    file_name = '.'.join(file_name)
    file_type = f[-1]
    if file_type.lower() == 'mp4':
        v.mp4 = v.video
        v.save()
        file_new = file_name + '.flv'
        out_file = join(out_path, file_new)
        comm = 'ffmpeg -i {0} -strict -2 {1}'.format(v.video.path, out_file)
        print comm
        os.system(comm)
        v.flv = 'videos/' + file_name + '.flv'
        v.save()

    elif file_type.lower() == 'flv':
        v.flv = v.video
        v.save()
        file_new = file_name + '.mp4'
        out_file = join(out_path, file_new)
        comm = 'ffmpeg -i {0} -strict -2 {1}'.format(v.video.path, out_file)
        print comm
        os.system(comm)
        v.mp4 = 'videos/' + file_name + '.mp4'
        v.save()


def transform_ppi(v):
    f = str(v.video).split('/')[-1].split('.')
    file_name = f[:-1]
    file_name = '.'.join(file_name)
    file_type = f[-1]

    target_ppi = "480*272"

    file_new = file_name + '_' + target_ppi + '.' + file_type
    source_file = join(source_path, file_name+'.'+file_type)
    out_file = join(out_path, file_new)
    comm = 'ffmpeg -i {0} -strict -2 -s {1} {2}'.format(source_file, target_ppi, out_file)# The Chinese charcters are not support
    print comm
    os.system(comm)
    v.low_ppi = 'videos/' + file_new
    v.save()


