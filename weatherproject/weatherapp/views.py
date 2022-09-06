from django.shortcuts import render
import requests 
import datetime
from weatherapp.models import alertlog
# Create your views here.

def index(request):

    logs = alertlog.objects.all()

    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'amsterdam'
    
    appid = ''
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {'q':'city','appid':appid,'units': 'Metric'}#,'units': 'Metric'
    r = requests.get(url=URL,params=PARAMS)

    res = r.json()
    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = res['main']['temp']

    day=datetime.date.today()
    
    if temp == 0:

        alertcity = city
        temp = temp
        desc = description
        log = alertlog(alertcity=alertcity,temp=temp,desc=desc).save()
        return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'temp':temp,'day':day,'city':city,'logs':logs})
    
    else:
      return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'temp':temp,'day':day,'city':city,'logs':logs})
    
    