from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^([0-9]+)/$', views.quotes, name='quotes'),
    url(r'^post_author/$', views.post_author, name='post_author'),
    url(r'^post_quote/$', views.post_quote, name='post_quote'),
    url(r'^search_quote$', views.search_quote, name='search_quote'),
]
