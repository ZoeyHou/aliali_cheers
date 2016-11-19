#coding:utf-8
import Image  
import os
   
def make_thumb(path, thumb_path, w, h):  
	"""生成缩略图"""  
	img = Image.open(path)  
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

def make_video_thumb(file_path, out_d_rate, out_file):
	command = "ffmpeg -ss 00:00:01 -i {0} -frames:v 1 -s {1}  {2}".format(file_path, out_d_rate, out_file)
	os.system(command)
  

if __name__ == '__main__':
	make_thumb('1.jpg', '2.jpg', 260, 200)
	make_video_thumb('123.mp4', '260*200', 'test.jpg')
