import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Artist, Rating


def index(request):
    return HttpResponse("Index")


def json_view(data):
    return HttpResponse(json.dumps(data), content_type="application/json")


def who_is(artist_id):
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Exception as e:
        raise Http404(e.message)
    return artist


def view_artist(request, artist_id):
    """
    Views a single artist.
    """
    artist = who_is(artist_id)
    return render(request, "artist.html", {"artist": artist})


def view_rating(request, artist_id):
    """
    Returns the current rating of an artist.
    """
    artist = who_is(artist_id)
    
    try:
        result = {
            "artist_id": artist_id,
            "average": artist.total_stars / artist.ratings,
            "ratings": artist.ratings
        }
    except ZeroDivisionError as e:
        result = {
            "artist_id": artist_id,
            "average": 0,
            "ratings": 0
        }
    return json_view(result)



def rate(request, artist_id, value):
    """
    Adds a rating on an artist.
    """
    artist = who_is(artist_id)
    
    value = float(value)
    
    rating = Rating(ip="n/a", value=value)
    rating.save()
    
    artist.total_stars += value
    artist.ratings += 1
    artist.save()
    
    result = {
        "status": "added",
        "value": value,
        "artist_id": artist_id,
        "average": artist.total_stars / artist.ratings,
        "ratings": artist.ratings
    }
    return json_view(result)
