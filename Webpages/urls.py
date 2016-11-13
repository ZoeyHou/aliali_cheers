from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^hello$', views.return_hello, name='return_hello'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^video$', views.video, name='video'),
    url(r'^playpage/(.+)/$', views.playpage, name='playpage'),
    url(r'^playpage/(.+)/barrage$', views.barrage, name='barrage'),
    url(r'^$', views.index, name='index'),
]