from django.shortcuts import render
from django.http import HttpResponse
import datetime
import calendar
from calendar import HTMLCalendar


# Create your views here.
def home(request) :
    now = datetime.datetime.now()
    time = now.strftime("%H:%M %p")
    date = now.strftime("%d-%m-%Y")
    month = now.strftime("%m")
    year = now.strftime("%Y")
    year = int(year)
    month = int(month)

    mon = request.GET.get('month')
    yr = request.GET.get('year')

    try :
        if mon :
            month = int(mon)
        if yr :
            year = int(yr)
        cal = HTMLCalendar().formatmonth(year, month)
    except Exception as e :
        cal = ''
        print (f'error generating calander {mon} month and {yr}')



    context = {'date': date, 
               'time': time, 
               'month': month, 
               'year': year, 
               'cal' : cal
            }
    # return HttpResponse(html)
    # return HttpResponse('hiii')
    return render(request, 'index.html', context)