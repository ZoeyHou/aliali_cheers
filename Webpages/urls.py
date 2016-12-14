from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^hello/$', views.return_hello, name='return_hello'),
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^picture_display/(.+)/$', views.picture_display, name='picture_display'),
    url(r'^audio/', views.audio, name='audio'),
    url(r'^audio_playpage/(.+)/$', views.audio_playpage, name='audio_playpage'),
    url(r'^video/$', views.video, name='video'),
    url(r'^personal_page/(.+)/(.+)$', views.more_upload, name='more_upload'),
    url(r'^playpage/(.+)/$', views.playpage, name='playpage'),
    url(r'^playpage/(.+)/barrage$', views.barrage, name='barrage'),
    url(r'^like_collect/$', views.like_and_collect, name='like_and_collect'),
    url(r'^personal_page/(.+)/$', views.personal_page, name='personal_page'),
    url(r'^edit_info/$', views.edit_info, name='edit_info'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about_us/$', views.about_us, name='about_us'),
    url(r'^$', views.index, name='index'),

]