from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^user/', views.index, name='user'),
    url(r'^artist/(?P<artist_id>[0-9]+)/$', views.view_artist, name='view_artist'),
    url(r'^api/rate/(?P<artist_id>[0-9]+)/$', views.view_rating, name='view_rating'),
    url(r'^api/rate/(?P<artist_id>[0-9]+)/(?P<value>[0-9\\.]+)/$', views.rate, name='rate'),
    url(r'^api/review/(?P<artist_id>[0-9]+)/$', views.add_review, name='rate')
]
