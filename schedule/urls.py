from unicodedata import name
from django.urls import path
from . import views
from schedule import views as schedule_views

app_name = 'schedule'

urlpatterns = [
    path('', views.index, name='schedule'),
    path('changeschedule/<day>', schedule_views.changeschedule),
    path('schedule/create', schedule_views.create),
    # path('schedule/<int:thisday>', schedule_views.changeschedule),
]