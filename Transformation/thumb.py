# coding:utf-8
import Image
import os
from mutagen import File

def get_audio_cover(audio_file, cover_path):
    audio = File(audio_file)  # mutagen can automatically detect format and type of tags
    audio_tags = audio.tags.get('APIC:', '')
    if audio_tags:
        artwork = audio_tags.data  # access APIC frame and grab the image
        with open(cover_path, "wb") as cover:
            cover.write(artwork)
        return True
    else:
        return False


def make_thumb(image, thumb_path, w=260, h=200):
    """生成缩略图"""
    img = Image.open(image)
    width, height = img.size
    # 裁剪图片成正方形
    if width > height:
        delta = (width - height) / 2
        box = (delta, 0, width - delta, height)
        region = img.crop(box)
    elif height > width:
        delta = (height - width) / 2
        box = (0, delta, width, height - delta)
        region = img.crop(box)
    else:
        region = img

    thumb = region.resize((w, h), Image.ANTIALIAS)

    thumb.save(thumb_path, quality=70)


def make_video_thumb(file_path, out_file, out_d_rate='260*200'):
    command = "ffmpeg -ss 00:00:01 -i {0} -frames:v 1 -s {1}  {2}".format(file_path, out_d_rate, out_file)
    os.system(command)

