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