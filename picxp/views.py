from django.shortcuts import render, redirect
from django.http  import HttpResponse,  Http404
import datetime as dt
from .models import Image, Location


def index(request):
    date = dt.date.today()
    images = Image.all_pics()
    return render(request, 'all-pics/index.html', {"date": date, "images": images})

def image(request,image_id):
    try:
        image = Image.object.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/image.html"), {"image": image}

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{search_term}"
        print(searched_images)

        return render(request, 'all-pics/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})