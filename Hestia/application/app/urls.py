from django.urls import path
from . import views

urlpatterns = [
	path('about', views.indexAbout, name='about'),
	path('', views.indexMain, name='main'),
    path('dividend', views.indexDividend, name='dividend'),
	path('help', views.indexHelp, name='help'),
	path('main/data', views.indexMainData, name='main data')
]