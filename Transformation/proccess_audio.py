# -*- coding: UTF-8 -*-

import os
from os.path import join
from django.conf import settings

from Webpages.models import Video

source_path = settings.MEDIA_ROOT + 'audios'
out_path = settings.MEDIA_ROOT + 'audios'

def transform_format(a):
    file_name, file_type = str(a.audio).split('/')[-1].split('.')
    if file_type.lower() == 'mp3':
        a.mp3 = a.audio
        a.save()
        file_new = file_name + '.wav'
        out_file = join(out_path, file_new)
        comm = 'ffmpeg -i {0} {1}'.format(a.audio.path, out_file)
        print comm
        os.system(comm)
        a.wav = 'audios/' + file_name + '.wav'
        a.save()

    elif file_type.lower() == 'wav':
        a.wav = a.audio
        a.save()
        file_new = file_name + '.mp3'
        out_file = join(out_path, file_new)
        comm = 'ffmpeg -i {0} {1}'.format(a.audio.path, out_file)
        print comm
        os.system(comm)
        a.mp3 = 'audios/' + file_name + '.mp3'
        a.save()



