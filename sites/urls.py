from django.urls import path
from . import views

app_name = 'sites'

urlpatterns = [
    path('',views.main, name='main'),
    path('about/',views.about, name='about'),
    path('map/',views.map, name='map'),

]