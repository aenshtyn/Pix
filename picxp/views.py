from django.shortcuts import render, redirect
from django.http  import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def latest_pics(request):
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return render(request, 'all-pics/latest-pics.html', {"date": date,})

def picture(request,picture_id):
    try:
        picture = Picture.object.get(id = picture_id)
    except DoesNotExist:
        raise Htto404()
    return render(request,"all-pics/picture.html"), {"picture": picture}

