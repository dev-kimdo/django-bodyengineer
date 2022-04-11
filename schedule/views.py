from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
import calendar
from datetime import datetime, date
from .models import Schedule
import requests
from json import dumps

# Create your views here.

def index(request):
  schedules = Schedule.objects.all().order_by('time')
  schedule = Schedule.objects.get(date ='2022-03-05', name = 'yuri')
  # schedule = Schedule.objects.get(date='2022-03-05')
  htmlcalendar = calendar.HTMLCalendar(calendar.SUNDAY)
  s = htmlcalendar.formatmonth(2022,3)
  firstday = calendar.weekday(2022, 3, 1)
  today = date.today()
  thatday = date(2022,3,1)
  dataDictionary = {
        'hello': 13,
        'geeks': 'forgeeks',
        'ABC': 123,
        456: 'abc',
        14000605: 1,
        'list': ['geeks', 4, 'geeks'],
        'dictionary': {'you': 'can', 'send': 'anything', 3: 1}
    }
    # dump data
  dataJSON = dumps(dataDictionary)
  context = {'s' : s, 'today' : today, 'firstday' : firstday, 'schedules' : schedules, 'schedule' : schedule, 'thatday' : thatday, 'data': dataJSON}
  return render(request, 'schedule/index.html', context)

def changeschedule(request, day):
  content = {
    "day" : day
  }
  return render(request, 'schedule/changeschedule.html', content)

def create(request):
  print(request.GET)
  name = request.GET.get('username')
  date = request.GET.get('today')
  time = request.GET.get('chk')

  schedule = Schedule(name=name, date=date, time = time)
  schedule.save()
  # context = {'time' : request.GET['chk']}
  return redirect('/schedule', schedule_name=schedule.name)
  



