#coding:utf-8
import os
from PIL import Image, ImageFilter, ImageEnhance

def open_save(open_file, save_file):
    im = Image.open(open_file)
    im.save(save_file)

def handle(open_file,save_file,choice,value):
    im = Image.open(open_file)

    if choice == 'brightness':
        brightness = ImageEnhance.Brightness(im)
        bright_img = brightness.enhance(value)    # 亮度增强
        bright_img.save(save_file)

    if choice == 'sharpness':
        sharpness = ImageEnhance.Sharpness(im)
        sharp_img = sharpness.enhance(value)  # 锐度增强
        sharp_img.save(save_file)

    if choice == 'contrast':
        contrast = ImageEnhance.Contrast(im)
        contrast_img = contrast.enhance(value)  # 对比度增强
        contrast_img.save(save_file)

def set_filter(open_file,save_file,choice):   #choice: ImageFilter.BLUR|ImageFilter.CONTOUR|ImageFilter.DETAIL|ImageFilter.EDGE_ENHANCE|ImageFilter.EDGE_ENHANCE_MORE
    im = Image.open(open_file)                #ImageFilter.EMBOSS|ImageFilter.FIND_EDGES|ImageFilter.SMOOTH|ImageFilter.SMOOTH_MORE|ImageFilter.SHARPEN
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
    im0 = im.filter(item)
    im0.save(save_file)

def mode_convert(open_file,save_file,mode):    #mode: 1|L|P|RGB|RGBA|CMYK|YCbCr|I|F
    im = Image.open(open_file)
    im0 = im.convert(mode)
    im0.save(save_file)

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


