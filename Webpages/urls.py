from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^hello$', views.return_hello, name='return_hello'),
    url(r'^gallery$', views.gallery, name='gallery'),
    url(r'^audio/', views.audio, name='audio'),
    url(r'^video$', views.video, name='video'),
    url(r'^playpage/(.+)/$', views.playpage, name='playpage'),
    url(r'^playpage/(.+)/barrage$', views.barrage, name='barrage'),
    url(r'^personal_page$', views.personal_page, name='personal_page'),
    url(r'^search$', views.search, name='search'),
    url(r'^$', views.index, name='index'),
]