from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',home,name='blog_home'),
    url(r'^post/(?P<id>\d+)/$',Detail,name="blog_detail"),
]