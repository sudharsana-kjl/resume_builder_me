from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
	url(r'^$', views.index),
    url(r'^signin$', views.signin),
    url(r'^about/$', views.about),
    url(r'^logout$', views.logout_view),
    url(r'^my_resume$', views.my_resume),
    url(r'^new_resume$', views.new_resume),
    url(r'^edit_resume$', views.edit_resume),
    url(r'^delete_resume$', views.delete_resume),
]
