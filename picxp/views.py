from django.shortcuts import render, redirect
from django.http  import HttpResponse,  Http404
import datetime as dt
from .models import Picture


def latest_pics(request):
    date = dt.date.today()
    pics = Picture.pics_new()
    return render(request, 'all-pics/latest-pics.html', {"date": date,"pics":pics})

def picture(request,picture_id):
    try:
        picture = Picture.object.get(id = picture_id)
    except DoesNotExist:
        raise Htto404()
    return render(request,"all-pics/picture.html"), {"picture": picture}

