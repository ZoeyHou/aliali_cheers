#coding:utf-8
import os
from PIL import Image, ImageFilter

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

filter_list = ('EMBOSS', 'FIND_EDGES', 'SMOOTH', 'SMOOTH_MORE', 'SHARPEN')
model_type = ("<class 'Authentication.models.User'>", )

def open_save(open_file, save_file):
    im = Image.open(open_file)
    im.save(save_file)

def apply_filter(model,choice):   #choice: ImageFilter.BLUR|ImageFilter.CONTOUR|ImageFilter.DETAIL|ImageFilter.EDGE_ENHANCE|ImageFilter.EDGE_ENHANCE_MORE
    if str(type(model)) not in model_type:
        im = Image.open(model.cover.path)
    else:
        im = Image.open(model.avatar.path)
    item = ImageFilter.EMBOSS
    if choice == 'EMBOSS':
        item = ImageFilter.EMBOSS
    elif choice == 'FIND_EDGES':
        item = ImageFilter.FIND_EDGES
    elif choice == 'SMOOTH':
        item = ImageFilter.SMOOTH
    elif choice == 'SMOOTH_MORE':
        item = ImageFilter.SMOOTH_MORE
    elif choice == 'SHARPEN':
        item = ImageFilter.SHARPEN
    im = im.filter(item)
    if str(type(model)) not in model_type:
        im.save(model.cover.path)
    else:
        im.save(model.avatar.path)

def comlete_type(pic_model, type):
    dir_path, file_name = os.path.split(pic_model.picture.path)
    file_name = os.path.splitext(file_name)[0]
    file = open(pic_model.picture.path)
    if type == 'JPEG':
        open_save(file, dir_path + '/' + file_name + '.png')
        open_save(file, dir_path + '/' + file_name + '.gif')
        open_save(file, dir_path + '/' + file_name + '.bmp')
        pic_model.jpg = pic_model.picture
        pic_model.png = 'pictures/' + file_name + '.png'
        pic_model.gif = 'pictures/' + file_name + '.gif'
        pic_model.bmp = 'pictures/' + file_name + '.bmp'
        pic_model.save()
    elif type == 'GIF':
        open_save(file, dir_path + '/' + file_name + '.jpg')
        open_save(file, dir_path + '/' + file_name + '.png')
        open_save(file, dir_path + '/' + file_name + '.bmp')
        pic_model.gif = pic_model.picture
        pic_model.png = 'pictures/' + file_name + '.png'
        pic_model.jpg = 'pictures/' + file_name + '.jpg'
        pic_model.bmp = 'pictures/' + file_name + '.bmp'
        pic_model.save()
    elif type == 'PNG':
        open_save(file, dir_path + '/' + file_name+'.jpg')
        open_save(file, dir_path + '/' + file_name + '.gif')
        open_save(file, dir_path + '/' + file_name + '.bmp')
        pic_model.png = pic_model.picture
        pic_model.jpg = 'pictures/' + file_name + '.jpg'
        pic_model.gif = 'pictures/' + file_name + '.gif'
        pic_model.bmp = 'pictures/' + file_name + '.bmp'
        pic_model.save()
    elif type == 'BMP':
        open_save(file, dir_path + '/' + file_name + '.jpg')
        open_save(file, dir_path + '/' + file_name + '.gif')
        open_save(file, dir_path + '/' + file_name + '.png')
        pic_model.bmp = pic_model.picture
        pic_model.png = 'pictures/' + file_name + '.png'
        pic_model.gif = 'pictures/' + file_name + '.gif'
        pic_model.jpg = 'pictures/' + file_name + '.jpg'
        pic_model.save()


