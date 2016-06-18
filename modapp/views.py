from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Artist


def index(request):
    return HttpResponse("Index")


def view_artist(request, artist_id):
    """
    Views a single artist.
    """
    try:
        artist = Artist.objects.get(pk=artist_id)
    except:
        raise Http404("Artist not found")
    return render(request, "artist.html", {"artist": artist})
