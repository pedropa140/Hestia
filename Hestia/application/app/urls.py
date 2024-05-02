from django.urls import path
from . import views

urlpatterns = [
	path('about', views.indexAbout, name='about'),
	path('', views.indexMain, name='main'),
    path('dividend', views.indexDividend, name='dividend'),
    path('company', views.indexCompany, name='company'),
    path('companies', views.indexCompanies, name='companies'),
    path('api/tickers/', views.get_company_tickers, name='get_company_tickers'),
    path('api/ticker-data/<str:ticker>/', views.get_ticker_data, name='get_ticker_data'),
    path('api/ticker-book_to_share/<str:ticker>/', views.get_book_to_share_picture, name='get_book_to_share_picture'),
    path('api/ticker-current_ratio/<str:ticker>/', views.get_current_ratio_picture, name='get_current_ratio_picture'),
    path('api/ticker-debt_ratio/<str:ticker>/', views.get_debt_ratio_picture, name='get_debt_ratio_picture'),
    path('api/ticker-dividend_yield/<str:ticker>/', views.get_dividend_yield_picture, name='get_dividend_yield_picture'),
    path('api/ticker-earnings_per_share/<str:ticker>/', views.get_earnings_per_share_picture, name='get_earnings_per_share_picture'),
    path('api/ticker-stock_prices/<str:ticker>/', views.get_stock_prices_pictures, name='get_stock_prices_pictures'),
    path('api/csv/<str:ticker>/', views.DownloadCSV.as_view(), name='download_csv')
]