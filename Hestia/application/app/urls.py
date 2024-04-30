from django.urls import path
from . import views

urlpatterns = [
	path('about', views.indexAbout, name='about'),
	path('', views.indexMain, name='main'),
    path('dividend', views.indexDividend, name='dividend'),
    path('company', views.indexCompany, name='company'),
    path('companies', views.indexCompanies, name='companies'),
    path('api/tickers/', views.get_company_tickers, name='get_company_tickers'),

]