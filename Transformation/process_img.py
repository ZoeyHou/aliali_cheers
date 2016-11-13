#coding:utf-8


from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageEnhance


def open_save(open_file, save_file):
    im = Image.open(open_file)
    im.save(save_file)

def img_copy(open_file,save_file):
    im = Image.open(open_file)
    im0 = im.copy()
    im0.show()
    im0.save(save_file)

def print_info(open_file):
    im = Image.open(open_file)
    print "format: " + str(im.format)
    print "size: " + str(im.size)
    print "mode: " + str(im.mode)

def cut_img(open_file,save_file,box):    #box: (,,,,)
    im = Image.open(open_file)
    im_cut = im.crop(box)
    im_cut.show()
    im_cut.save(save_file)
    return im_cut

#################未使用#####################################
def img_paste(open_file,save_file,box,angle):
    im = Image.open(open_file)
    cut = cut_img(open_file,save_file,box)
    im.paste(cut,box)
    im.show()
    im.save(save_file)

def im_rotate(open_file,save_file,angle):
    im = Image.open(open_file)
    im0 = im.rotate(angle)  # 顺时针角度表示
    im0.show()
    im0.save(save_file)
    return im0

#################未使用#####################################
def im_transpose(open_file,save_file,choice,rotate):    #rotate: Image.ROTATE_90|120|180
    im = Image.open(open_file)      #out = im0.transpose(Image.FLIP_LEFT_RIGHT)   #out = im0.transpose(Image.FLIP_TOP_BOTTOM)
    im0 = im.transpose(rotate)
    im0.show()
    im0.save(save_file)

def change_size(open_file,save_file,size):      #size:(,)     只能缩小
    im = Image.open(open_file)
    print "before: " + str(im.size)
    im.thumbnail(size)
    print "after" + str(im.size)
    im.show()
    im.save(save_file)

def change_size_(open_file,save_file,size):      #size:(,)   可放大可缩小
    im = Image.open(open_file)
    print "before: " + str(im.size)
    im0 = im.resize((size), Image.ANTIALIAS)
    print "after" + str(im0.size)
    im0.show()
    im0.save(save_file)

def set_RGB(open_file,save_file,set_choose):      #rgb = (,,)
    im = Image.open(open_file)
    r, g, b = im.split()
    if set_choose == 'rgb':
        im0 = Image.merge("RGB", (r, g, b))
    if set_choose == 'rbg':
        im0 = Image.merge("RGB", (r, b, g))
    if set_choose == 'grb':
        im0 = Image.merge("RGB", (g, r, b))
    if set_choose == 'gbr':
        im0 = Image.merge("RGB", (g, b, r))
    if set_choose == 'bgr':
        im0 = Image.merge("RGB", (b, g, r))
    if set_choose == 'brg':
        im0 = Image.merge("RGB", (b, r, g))

    im0.show()
    im0.save(save_file)

def handle(open_file,save_file,choice,value):
    im = Image.open(open_file)

    if choice == 'brightness':
        brightness = ImageEnhance.Brightness(im)
        bright_img = brightness.enhance(value)    # 亮度增强
        bright_img.show()
        bright_img.save(save_file)

    if choice == 'sharpness':
        sharpness = ImageEnhance.Sharpness(im)
        sharp_img = sharpness.enhance(value)  # 锐度增强
        sharp_img.show()
        sharp_img.save(save_file)

    if choice == 'contrast':
        contrast = ImageEnhance.Contrast(im)
        contrast_img = contrast.enhance(value)  # 对比度增强
        contrast_img.show()
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

####################缺少处理字体的包#####################
def add_text(open_file,save_file,font_file = 'E:\python-works\image_transfer\simhei.ttf',font_size = 20):
    im = Image.open(open_file)
    ttfont = ImageFont.truetype(font_file, font_size)
    draw = ImageDraw.Draw(im)
    draw.text((10, 10), u'圈圈组', fill=(0, 0, 0), font=ttfont)
    draw.text((40, 40), unicode('多媒体', 'utf-8'), fill=(0, 0, 0), font=ttfont)
    im.show()
    im.save(save_file)


# if __name__ == "__main__":
#     path = '8.png'
#     format_ = 'png'
#     function_choice = 'choose'
#
# #raw_input 结果有''，input结果无''
#     while(function_choice != 'exit'):
#         function_choice = str(raw_input(u"Please input your choice: "))
#         if function_choice == 'open_save':
#             open_save(path, '%s.%s' %(function_choice,format_))
#             print "DONE!"
#
#         if function_choice == 'img_copy':
#             img_copy(path, '%s.%s' %(function_choice,format_))
#             print "DONE!"
#
#         if function_choice == 'print_info':
#             print_info(path)
#             print "DONE!"
#
#         if function_choice == 'cut_img':
#             num_in = input(u"Seperated by ,: ")     #Seperated by ,: 100,100,200,200  得到的是tuple
#             #print num_in
#             cut = cut_img(path, '%s.%s' %(function_choice,format_), num_in)
#             print "DONE!"
#
#         if function_choice == 'img_paste':  ##############暂时无大的意义##############
#             img_paste(path, '%s.%s' %(function_choice,format_), (120,130,140,150))
#             print "DONE!"
#
#         if function_choice == 'im_rotate':
#             angle = int(raw_input(u"Please input your angle: "))
#             im_rotate(path, '%s_%s.%s' %(function_choice,str(angle),format_),angle)
#             print "DONE!"
#
#         if function_choice == 'change_size':
#             num_in = input(u"Seperated by ,: ")
#             # print num_in
#             change_size(path, '%s.%s' %(function_choice,format_),num_in)
#             print "DONE!"
#
#         if function_choice == 'change_size_':
#             num_in = input(u"Seperated by ,: ")
#             # print num_in
#             change_size_(path, '%s.%s' %(function_choice,format_),num_in)
#             print "DONE!"
#
#         if function_choice == 'set_RGB':
#             choice = str(raw_input(u"Please input your choice: "))
#             set_RGB(path, '%s%s.%s' % (function_choice, choice, format_), choice)
#             print "DONE!"
#
#         if function_choice == 'handle':
#             choice = str(raw_input(u"Please input your choice: "))
#             value = float(raw_input(u"Please input your value: "))
#             handle(path, '%s_%s%s.%s' %(function_choice,choice,str(value),format_),choice,value)
#             print "DONE!"
#
#         if function_choice == 'set_filter':
#             choice = input(u"Please input your choice: ")
#             set_filter(path, '%s_%s.%s' %(function_choice,choice,format_),choice)
#             print "DONE!"
#
#         if function_choice == 'mode_convert':
#             mode = str(raw_input(u"Please input your choice: "))
#             mode_convert(path, '%s_%s.%s' %(function_choice,mode,format_),mode)
#             print "DONE!"
#
#
