from django.conf.urls import url

from . import views
import Webpages.views


urlpatterns = [
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.login, name='login'),
]