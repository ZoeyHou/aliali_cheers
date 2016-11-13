from django.conf.urls import url

from . import views


urlpatterns = [
    #url(r'^hh$', views.return_hello, name='return_hello'),
    url(r'^uploadp/$', views.upload_picture, name='upload_picture'),
    url(r'^uploadv/$', views.upload_video, name='upload_video'),
    url(r'^process_p/$', views.process_img, name='process_img'),
    url(r'^process_v/$', views.process_video, name='process_video'),
]
