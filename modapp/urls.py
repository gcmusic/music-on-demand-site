from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^user/', views.index, name='user'),
    url(r'^artist/(?P<artist_id>[0-9]+)/$', views.view_artist, name='view_artist')
]
