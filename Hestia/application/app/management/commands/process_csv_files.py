import multiprocessing
import os
import csv
import logging
from datetime import datetime
from django.core.management import BaseCommand
from django.apps import apps
from django.db import models
from django.db import connection
from django.db.utils import OperationalError
from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from django.db import transaction
from django.db.models import F
from operator import attrgetter
from app.models import TickerData, CompanyTicker  # Import your models from the 'app' module

logging.basicConfig(level=logging.INFO) 

processed_tickers = set()

def convert_to_float(value, default=-1.0):
    return float(value.strip()) if value.strip() else default

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
    dividend_yield = convert_to_float(row.get('dividend_yield_ratio', '-1.0'))
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

batched_tickers = []
    
def process_csv_file(csv_file_path):
    ftick = os.path.basename(csv_file_path).split('.')[0].upper()
    
    if ftick in processed_tickers:
        logging.info(f"Skipping {ftick} data: already processed")
        return
    
    processed_tickers.add(ftick)
    
    logging.info(f"{csv_file_path}")
    try:
        company_name = CompanyTicker.objects.get(ticker=ftick).company_name
    except CompanyTicker.DoesNotExist:
        company_name = get_company_name(csv_file_path)
        
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        with ThreadPoolExecutor(max_workers=30) as executor:
            # Submit each row to be processed asynchronously
            futures = [executor.submit(process_row, ftick, company_name, row) for row in csv_reader]
    
            # Wait for all futures to complete
            for future in futures:
                future.result()
                
        logging.info(f"Processed {ftick} data")
    
processed_tickers_file = "processed_tickers.txt"

def process_all(csv_file_paths):
    num_cores = multiprocessing.cpu_count()
    max_workers = 30 + num_cores * 4  # Adjust based on your system's capabilities
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks for each CSV file to be processed concurrently
        futures = [executor.submit(process_csv_file, csv_file_path) for csv_file_path in csv_file_paths]    
        # Wait for all tasks to complete
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                
    logging.info("Pushing TickerData objects into database...")
    sorted_tickers = sorted(batched_tickers, key=attrgetter('ticker', 'start_date'))
    TickerData.objects.bulk_create(sorted_tickers)  # Save any remaining ticker data in the batched list

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
        
        processed_tickers = self.load_processed_tickers()
            
        try:
            process_all(csv_file_paths)
        except KeyboardInterrupt:
            logging.info("Interrupted by user. Saving processed tickers.")
            self.save_processed_tickers(processed_tickers)
            raise  # Re-raise KeyboardInterrupt to exit gracefully

        # Save processed tickers
        self.save_processed_tickers(processed_tickers)
                    
                    