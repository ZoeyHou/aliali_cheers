from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^recog_login/$', views.recog_login, name='recog_login'),
    url(r'^recog_register/$', views.recog_register, name='recog_register'),
    url(r'^$', views.login, name='login'),
]