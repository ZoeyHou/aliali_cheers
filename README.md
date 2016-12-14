# aliali_chrees
计划完成的：
	[把发给老师的复制过来]

目前完成的部分：
	*127.0.0.1:8000/admin：后台数据库管理 用户名：suprejiji 密码：guoji1420
	*127.0.0.1:8000/gllary： 相片界面：上传，格式、模式转换，滤镜。
	*127.0.0.1:8000/video： 上传，视频格式，分辨率转换，视频播放（含弹幕）。
	
工作及文档分配：
	×陈：人脸识别登录
	×丁：播放器，弹幕
	×刘：人脸识别登录
	×侯：前端设计
	×熊：后台及整合
	×杨：聊天
	×张：视频图像处理，人脸识别登录


可通过如下方法跑起网站来：
Ｗindows：
	1. 安装python django PIL ffmpeg
	可以参照以下教程装上django，开发用的django是1.9.6版本, 之上到1.10.4都是可以跑的起来的。
		http://jingyan.baidu.com/article/466506580e7d29f549e5f8b6.html
	需要python的PIL库，安装如下：
		在32位win7下可以通过下面的地址下载windows安装程序来安装：
		http://www.pythonware.com/products/pil/
		但是64位的程序官方没有提供，需要到第三方地址下载安装。
		http://www.lfd.uci.edu/~gohlke/pythonlibs/
	需要安装ffmpeg，教程如下：
		http://zh.wikihow.com/%E5%9C%A8Windows%E4%B8%8A%E5%AE%89%E8%A3%85FFmpeg%E7%A8%8B%E5%BA%8F

	2. cd到项目文件夹下
	3. 输入 python manage.py runserver
	4. 浏览器访问 127.0.0.1:8000

Ｌinux：
	1. 安装python django PIL ffmpeg
		Ubuntu下： 
			PIL ffmpeg： 
				sudo apt-get install python-imaging ffmpeg
			django： 
				sudo apt-get install pip
				sudo pip install django==1.9.6
			python:系统自带了
						
	2. cd到项目文件夹下
	3. 输入 python manage.py runserver
	4. 浏览器访问 127.0.0.1:8000

MAC：
	1. 安装python django PIL ffmpeg
	2. cd到项目文件夹下
	3. 输入 python manage.py runserver
	4. 浏览器访问 127.0.0.1:8000
	

