from django.shortcuts import render, redirect
from django.http  import HttpResponse,  Http404
import datetime as dt
from .models import Image, Location


def index(request):
    images = Image.all_pics()
    locations = Location.all_locations()

    return render(request, 'index.html', {"locations": locations, "images": images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_category(category)
        message = f"{category}"
        print(searched_images)

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any category"
        return render(request, 'search.html',{"message":message})


def location_captured (request, location):
    pics = Image.images_by_location(location)
    print(pics)

    return render (request, 'location.html', {'location_pics': pics})