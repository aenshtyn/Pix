from django.shortcuts import render, redirect
from django.http  import HttpResponse,  Http404
import datetime as dt
from .models import Picture


def index(request):
    date = dt.date.today()
    pics = Picture.objects.all()
    return render(request, 'all-pics/index.html', {"date": date,"pics":pics})

def picture(request,picture_id):
    try:
        picture = Picture.object.get(id = picture_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-pics/picture.html"), {"picture": picture}

