from django.core.management import BaseCommand
from app.models import CompanyTicker
from _scripts_.read_div_info import read_csv_multithreaded 
from concurrent.futures import ThreadPoolExecutor



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        company_tickers = read_csv_multithreaded()  # Use your multithreading function to get tickers info

        # Bulk create CompanyTicker objects in the database
        CompanyTicker.objects.bulk_create(company_tickers)

        self.stdout.write(self.style.SUCCESS('Batch processing completed. CompanyTicker objects pushed to database.'))