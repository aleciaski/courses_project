from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^courses/(?P<id>\d+)/destroy$', views.destroy)
      # This line has changed! Notice that urlpatterns is a list, the comma is in
] 