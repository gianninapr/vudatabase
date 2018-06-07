from django.conf.urls import include, url
from django.contrib import admin
from . import views

app_name = "stars"
urlpatterns = [
	url(r'^star/(?P<pk>\d+)$', views.Detail.as_view(), name= 'detail'),
]