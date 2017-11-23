from django.conf.urls import include, url
from app.views import *
# from django.contrib import admin

urlpatterns = [
    url(r"^api/",api, name="api"),
]