import os
import csv
from datetime import datetime
from django.core.management import BaseCommand
from django.apps import apps
from django.db import models
from django.db import connection
from django.db.utils import OperationalError
from app.models import TickerData, CompanyTicker  # Import your models from the 'app' module

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

class Command(BaseCommand):
    help = 'Create custom tables for each ticker based on CSV data'

    def handle(self, *args, **options):
        csv_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../stockdata/div_info'))
        csv_files = [f for f in os.listdir(csv_dir) if f.endswith('.csv')]

        for csv_file in csv_files:
            ticker_symbol = os.path.splitext(csv_file)[0]  # Extract ticker symbol from file name
            dynamic_model = create_dynamic_model(ticker_symbol)

            # Register the model
            apps.all_models['app'][f'DynamicTickerData_{ticker_symbol}'] = dynamic_model

            # print(f'Processing {csv_file}...')
            # Assuming dynamic_model is already defined
            table_name = dynamic_model._meta.db_table

            # Check if the table exists
            try:
                with connection.cursor() as cursor:
                    cursor.execute(f"SELECT 1 FROM {table_name} LIMIT 1")
                table_exists = True
            except OperationalError:
                table_exists = False

            # If the table doesn't exist, create it
            if not table_exists:
                with connection.schema_editor() as schema_editor:
                    schema_editor.create_model(dynamic_model)
                
            # Now, let's read the CSV file and create TickerData instances
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                # Assuming CSV columns are named similarly to TickerData fields
                    company_ticker = CompanyTicker.objects.get(ticker=row['ticker'])
                    start_date = datetime.strptime(row['start_date'], '%Y-%m-%d').date()

                    
                    

                    # Create TickerData instance
                    ticker_data = TickerData(
                        ticker=company_ticker,
                        company_name = CompanyTicker.objects.get(ticker=company_ticker).company_name,  # Assuming company_name is the same as ticker
                        start_date=start_date,
                        end_date=datetime.strptime(row['end_date'], '%Y-%m-%d').date(),
                        book_value=float(row['book_value']),
                        book_to_share_value=float(row['book_to_share_value']),
                        earnings_per_share=float(row['earnings_per_share']),
                        debt_ratio=float(row['debt_ratio']),
                        current_ratio=float(row['current_ratio']),
                        end_open=float(row['end_open']),
                        dividend_yield=float(row['dividend_yield']),
                        start_open=float(row['start_open']),
                        start_close=float(row['start_close']),
                        start_high=float(row['start_high']),
                        start_low=float(row['start_low']),
                        end_close=float(row['end_close']),
                        end_high=float(row['end_high']),
                        end_low=float(row['end_low']),
                        volume=float(row['volume'])
                    )

                    # Save the instance to the database
                    ticker_data.save()
                        
                    