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
    # path('api/ticker/<str:ticker>/chart/book_to_share/', views.get_book_to_share_picture, name='get_book_to_share_picture'),
    # path('api/ticker/<str:ticker>/chart/current_ratio', views.get_current_ratio_picture, name='get_current_ratio_picture'),
    # path('api/ticker/<str:ticker>/chart/debt_ratio', views.get_debt_ratio_picture, name='get_debt_ratio_picture'),
    # path('api/ticker/<str:ticker>/chart/dividend_yield', views.get_dividend_yield_picture, name='get_dividend_yield_picture'),
    # path('api/ticker/<str:ticker>/chart/earnings_per_share', views.get_earnings_per_share_picture, name='get_earnings_per_share_picture'),
    # path('api/ticker/<str:ticker>/chart/stock_prices', views.get_stock_prices_pictures, name='get_stock_prices_pictures'),
    path('api/ticker/<str:ticker>/chart/<str:chartname>/', views.chart, name='chart'),
    path('api/csv/<str:ticker>/', views.DownloadCSV.as_view(), name='download_csv')
]