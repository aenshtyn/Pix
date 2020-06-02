from django.shortcuts import render, redirect
from django.http  import HttpResponse,  Http404
import datetime as dt
from .models import Image


def index(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'all-pics/index.html', {"date": date,"images":images})

def image(request,image_id):
    try:
        image = Image.object.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/image.html"), {"image": image}

