import os
import csv
import logging
from datetime import datetime
from django.core.management import BaseCommand
from django.apps import apps
from django.db import models
from django.db import connection
from django.db.utils import OperationalError
from concurrent.futures import ThreadPoolExecutor, wait
from django.db import transaction
from app.models import TickerData, CompanyTicker  # Import your models from the 'app' module

logging.basicConfig(level=logging.INFO) 

processed_tickers = set()

def create_dynamic_model(ticker_symbol):
    class Meta:
        db_table = f'{ticker_symbol}_data'

    dynamic_model = type('DynamicTickerData', (models.Model,), {
        'ticker': models.CharField(max_length=4),
        'company_name': models.CharField(max_length=100),
        'start_date': models.DateField(default='1900-01-01', primary_key=True),
        'end_date': models.DateField(default='1900-01-01'),
        'book_value': models.FloatField(default=-1.0),
        'book_to_share_value': models.FloatField(default=-1.0),
        'earnings_per_share': models.FloatField(default=-1.0),
        'debt_ratio': models.FloatField(default=-1.0),
        'current_ratio': models.FloatField(default=-1.0),
        'end_open': models.FloatField(default=-1.0),
        'dividend_yield': models.FloatField(default=-1.0),
        'start_open': models.FloatField(default=-1.0),
        'start_close': models.FloatField(default=-1.0),
        'start_high': models.FloatField(default=-1.0),
        'start_low': models.FloatField(default=-1.0),
        'end_close': models.FloatField(default=-1.0),
        'end_high': models.FloatField(default=-1.0),
        'end_low': models.FloatField(default=-1.0),
        'volume': models.FloatField(default=-1.0),
        '__module__': __name__,
        'Meta': Meta,
    })

    return dynamic_model

def convert_to_float(value, default=-1.0):
    if value.strip():  # Check if the value is not empty after stripping whitespace
        return float(value)
    else:
        return default
    
batched_tickers = []

def process_row(ftick, company_name, row):
    ticker = ftick
    company_name = company_name
    start_date = row.get('start_date', '1900-01-01')
    end_date = row.get('end_date', '1900-01-01')
    book_value = convert_to_float(row.get('book_value', '-1.0'))
    book_to_share_value = convert_to_float(row.get('book_to_share_value', '-1.0'))
    earnings_per_share = convert_to_float(row.get('earnings_per_share', '-1.0'))
    debt_ratio = convert_to_float(row.get('debt_ratio', '-1.0'))
    current_ratio = convert_to_float(row.get('current_ratio', '-1.0'))
    end_open = convert_to_float(row.get('end_open', '-1.0'))
    dividend_yield = convert_to_float(row.get('dividend_yield', '-1.0'))
    start_open = convert_to_float(row.get('start_open', '-1.0'))
    start_close = convert_to_float(row.get('start_close', '-1.0'))
    start_high = convert_to_float(row.get('start_high', '-1.0'))
    start_low = convert_to_float(row.get('start_low', '-1.0'))
    end_close = convert_to_float(row.get('end_close', '-1.0'))
    end_high = convert_to_float(row.get('end_high', '-1.0'))
    end_low = convert_to_float(row.get('end_low', '-1.0'))
    volume = convert_to_float(row.get('volume', '-1.0'))

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
    except ValueError:
        start_date = datetime.strptime('1900-01-01', '%Y-%m-%d').date()
        end_date = datetime.strptime('1900-01-01', '%Y-%m-%d').date()

    ticker_data = TickerData(
        ticker=ticker,
        company_name=company_name,
        start_date=start_date,
        end_date=end_date,
        book_value=book_value,
        book_to_share_value=book_to_share_value,
        earnings_per_share=earnings_per_share,
        debt_ratio=debt_ratio,
        current_ratio=current_ratio,
        end_open=end_open,
        dividend_yield=dividend_yield,
        start_open=start_open,
        start_close=start_close,
        start_high=start_high,
        start_low=start_low,
        end_close=end_close,
        end_high=end_high,
        end_low=end_low,
        volume=volume
    )

    batched_tickers.append(ticker_data)
        
def get_company_name(csv_file_path):
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            return row.get('company_name', 'Unknown').title()
    
def process_csv_file(csv_file_path, ftick):
        try:
            company_name = CompanyTicker.objects.get(ticker=ftick).company_name
        except CompanyTicker.DoesNotExist:
            company_name = get_company_name(csv_file_path)
        if ftick in processed_tickers:
            logging.info(f"Skipping {ftick} data: already processed")
            return  # Skip processing if the ticker is already processed
            
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            # Create a ThreadPoolExecutor with 5 worker threads
            with ThreadPoolExecutor(max_workers=30) as executor:
                # Submit each row to be processed asynchronously
                futures = [executor.submit(process_row, ftick, company_name, row) for row in csv_reader]
        
                # Wait for all futures to complete
                for future in futures:
                    future.result()
                    
                wait(futures)

            logging.info(f"Processed {ftick} data")
        
        # Save the batched ticker data after processing CSV file
        save_batched_ticker_data()
          
def save_batched_ticker_data():
    # Use transaction.atomic() for batch saving
    with transaction.atomic():
        TickerData.objects.bulk_create(batched_tickers)
    
    # Clear the batched_ticker_data list after saving
    batched_tickers.clear()          
    
processed_tickers_file = "processed_tickers.txt"
class Command(BaseCommand):
    help = 'Create custom tables for each ticker based on CSV data'
    
    def load_processed_tickers(self):
        if not os.path.exists(processed_tickers_file):
            # Create the processed tickers file if it doesn't exist
            with open(processed_tickers_file, 'w'):
                pass  # Create an empty file
            
        with open(processed_tickers_file, 'r') as f:
            return set(line.strip() for line in f)

    def save_processed_tickers(self, processed_tickers):
        with open(processed_tickers_file, 'w') as f:
            for ticker in processed_tickers:
                f.write(f"{ticker}\n")

    def handle(self, *args, **options):
        csv_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../stockdata/div_info'))
        csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]
        csv_file_paths = [os.path.join(csv_dir, f) for f in csv_files]

        # Process each CSV file sequentially
        processed_tickers = self.load_processed_tickers()
        for csv_file_path in csv_file_paths:
            logging.info(f"{csv_file_path}")
            try:
                ftick = os.path.basename(csv_file_path).split('.')[0]
                if (ftick in processed_tickers):
                    logging.info(f"Skipping {ftick} data: already processed")
                    continue
                process_csv_file(csv_file_path, ftick)
                processed_tickers.add(ftick)
            except KeyboardInterrupt:
                logging.info("Interrupted by user. Saving processed tickers.")
                self.save_processed_tickers(processed_tickers)
                raise  # Re-raise KeyboardInterrupt to exit gracefully
            
        self.save_processed_tickers(processed_tickers)

                        
                    