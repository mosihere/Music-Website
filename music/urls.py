from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'music'
urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'), # Go and check index function in music views.py

    # /music/<album_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),
]
