# aliali_chrees  

## 每个app对应的功能：  
  
### webpage：  
对应项目目录下的webpage文件夹与url中的/*  
主要用于展示网站中所有页面，播放视频音频，展示图片，处理弹幕请求，处理评论，点赞，收藏，个人主页展示与编辑功能。  
### tranformation：  
对应目录下Transfomation文件夹与url中/transform/*  
主要处理多媒体文件的上传与上传后的转换。
### authentication：  
对应项目目录下Authentication文件夹与url中/login/*  
主要处理用户的登录/注册，人脸识别登录与注册。  

  
## 所有URL及其对应功能：  
*/  网站主页  
*/gallery/  所有图片展示页面  
*/picture_display/(.+)/  特定图片展示页面  
*/audio/  所有音频展示页面  
*/audio_playpage/(.+)/  特定音频播放页面  
*/video/  所有视频展示页面   
*/playpage/(.+)/  特定视频播放页面  
*/playpage/(.+)/barrage  收到带有视频地址的post请求后，这个链接会返回视频对应的弹幕文件。  
*/personal_page/(.+)/   用户的个人信息页面  
*/personal_page/(.+)/(.+) 用户收藏/上传所有文件展示页面，第一个(.+)是用户名，第二个(.+)是个人页面下对应的一些子页面，比如说个人上传的所有视频。 
*/like_collect/  当在观看一个视频/音频/图片的时候，如果用户点击收藏，点赞，踩三个按钮中的任意一个，都会向这个url发送一个post请求，用来记录用户的行为  
*/edit_info/  编辑用户信息的页面，同时在用户更改后，更新的信息需要post给这个url。  
*/search/  搜索（视频/音频/图片/用户）页面  
*/about_us/  团队信息展示页面  
  
*/admin：后台数据库管理 用户名：superjiji 密码：guoji1420  
  
*/transform/upload   任何文件上传都需要将数据post给这个url，其中调用了python-magic来判断文件类型，并根据此来决定对应的操作。同时在数据上传后，数据会在后台进行转换，使之支持多种文件格式，比如上传一个jpg文件后，后台会自动把这个文件转换为bmp，png等格式，提供给用户下载。   
  
*/login/ 登录的时候js会向这个链接发一个post请求，其中包含了用户名和密码，用于验证登录。  
*/login/register/  注册页面  
*/login/logout/  注销的时候js会向这个URL发送一个请求，服务器会指示客户端把登录时产生的cookie删除  
*/login/recog_login/  人脸识别登录  
*/login/recog_register  人脸识别注册  
  
  
## 工作及文档分配：  
具体可参见 /about_us  
  
×陈：人脸识别登录  
×丁：播放器，弹幕  
×刘：人脸识别登录  
×侯：前端设计  
×熊：后台及整合  
×杨：聊天  
×张：视频图像处理，人脸识别登录  


## 可通过如下方法跑起网站来：  
### Ｗindows：  
1. 安装python django PIL ffmpeg  
可以参照以下教程装上python pip.  
http://www.tuicool.com/articles/eiM3Er3/  
安装django，开发用的django是1.9.6版本, 之上到1.10.4都是可以跑的起来的。  
安装好pip后，cd 到项目文件夹，在cmd中输入  
`pip install -r requirement.txt`  
安装依赖的环境  
需要安装ffmpeg，教程如下：  
http://zh.wikihow.com/%E5%9C%A8Windows%E4%B8%8A%E5%AE%89%E8%A3%85FFmpeg%E7%A8%8B%E5%BA%8F  

2. cd到项目文件夹下  
3. 输入python manage.py makemigrations --empty Authentication Transformation Webpages  
4. 输入python makemigrations，然后输入python manage.py migrate  
5. 输入 python manage.py runserver  
6. 浏览器访问  127.0.0.1:8000  

### Linux：  
1. 安装python django PIL ffmpeg 以及其他依赖环境  
Ubuntu下：  
PIL ffmpeg：  
`sudo apt-get install ffmpeg `  
其他依赖环境：  
`pip install -r requirement.txt`  

2. cd到项目文件夹下  
3. 输入python manage.py makemigrations --empty Authentication Transformation Webpages  
4. 输入python makemigrations，然后输入python manage.py migrate  
5. 输入 python manage.py runserver  
6. 浏览器访问  127.0.0.1:8000  

### MAC：
1. 安装python pip django PIL ffmpeg  
2. cd到项目文件夹下, pip install -r requirement.txt  
3. 输入python manage.py makemigrations --empty Authentication Transformation Webpages  
4. 输入python makemigrations，然后输入python manage.py migrate
5. 输入 python manage.py runserver  
6. 浏览器访问  127.0.0.1:8000  

## 所有依赖的库
mmmpeg  
以及pip可安装的整理在requirement.txt中。  

## 网站具体效果展现与功能介绍  
请参见项目目录中/doc/presentation_ppt.pdf  
