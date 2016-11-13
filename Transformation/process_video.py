# -*- coding: UTF-8 -*-

import os
from os.path import join
from django.conf import settings

from Webpages.models import Video

source_path = settings.MEDIA_ROOT + 'videos'
out_path = settings.MEDIA_ROOT + 'videos'

def transform_format(file_name, target_fm, user):
    fm = file_name.split('.')[-1]

    file_new = file_name.replace('.'+fm, '.'+target_fm)
    source_file = join(source_path, file_name)
    out_file = join(out_path, file_new)
    comm = 'ffmpeg -i {0} -strict -2 {1}'.format(source_file, out_file)
    print comm
    os.system(comm)

    v = Video(user=user, video='videos/'+file_new)
    v.save()

def transform_ppi(file_name, target_ppi, user):
    fm = file_name.split('.')[-1]
    file_profix = file_name.split('.')[1]

    file_new = file_profix + '_' + target_ppi + '.' + fm
    source_file = join(source_path, file_name)
    out_file = join(out_path, file_new)
    comm = 'ffmpeg -i {0} -strict -2 -s {1} {2}'.format(source_file, target_ppi, out_file)
    print comm
    os.system(comm)

    v = Video(user=user, video='videos/'+file_new)
    v.save()

