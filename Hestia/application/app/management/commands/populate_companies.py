from django.core.management import BaseCommand
from app.models import CompanyTicker
from scripts.read_div_info import ticker_with_div

class Command(BaseCommand):
    help = 'Populate CompanyTicker model with data from tickers_with_dividends.csv'

    def handle(self, *args, **kwargs):
        tickers_info = ticker_with_div()
        for ticker, company_name in tickers_info.items():
            CompanyTicker.objects.get_or_create(ticker=ticker, company_name=company_name.strip())
