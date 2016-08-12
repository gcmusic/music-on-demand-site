import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import Artist, Rating, Review


def index(request):
    return HttpResponse('Index')


def json_view(data):
    return HttpResponse(json.dumps(data), content_type='application/json')


def who_is(artist_id):
    try:
        artist = Artist.objects.get(pk=artist_id)
    except Exception as e:
        raise Http404(e.message)
    return artist


def add_review(request, artist_id):
    """
    Adds a review on an artist.
    """
    response = {'status': ''}
    try:
        review_data = {
            'sender': request.POST['sender'],
            'subject': request.POST['subject'],
            'body': request.POST['body'],
            'submit_date': timezone.now(),
            'artist_id': artist_id
        }
        review = Review(**review_data)
        review.save()
        response['status'] = 'ok'
    except Exception as e:
        response['status'] = 'failed'
        response['details'] = e.message
    return json_view(response)


def view_artist(request, artist_id):
    """
    Views a single artist.
    """
    artist = who_is(artist_id)
    reviews = Review.objects.filter(artist_id=artist_id)
    return render(request, 'artist.html', {'artist': artist, 'reviews': reviews})


def view_rating(request, artist_id):
    """
    Returns the current rating of an artist.
    """
    try:
        artist = who_is(artist_id)
        result = {
            'artist_id': artist_id,
            'average': artist.total_stars / artist.ratings,
            'ratings': artist.ratings
        }
    except ZeroDivisionError as e:
        result = {
            'artist_id': artist_id,
            'average': 0,
            'ratings': 0
        }
    return json_view(result)


def rate(request, artist_id, value):
    """
    Adds a rating to an artist.
    """
    ip = request.META['REMOTE_ADDR']
    value = float(value)
    
    result = {}
    
    matching = Rating.objects.filter(ip=ip, artist_id=artist_id)
    if len(matching) > 0:
        result = {
            'status': 'already_exists'
        }
    else:    
        rating = Rating(ip=ip, value=value, artist_id=artist_id)
        rating.save()

        artist = who_is(artist_id)

        artist.total_stars += value
        artist.ratings += 1
        artist.save()
    
        result = {
            'status': 'added',
            'value': value,
            'ip': ip,
            'artist_id': artist_id,
            'average': artist.total_stars / artist.ratings,
            'ratings': artist.ratings
        }
    
    return json_view(result)
