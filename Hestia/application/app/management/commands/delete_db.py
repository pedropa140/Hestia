import os
import shutil
import time
from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting migrations and processed_tickers.txt...")
        
        # Delete datbase
        self.delete_database()

        # Delete migrations >= 0002
        self.delete_migrations()

        # Delete processed_tickers.txt file
        self.delete_processed_tickers()

        self.stdout.write(self.style.SUCCESS("Deletion completed."))

    def delete_migrations(self):
        migration_path = os.path.join(settings.BASE_DIR, "app", "migrations")
        for filename in os.listdir(migration_path):
            if filename.startswith("0002"):
                migration_file = os.path.join(migration_path, filename)
                if os.path.isdir(migration_file):
                    shutil.rmtree(migration_file)
                    self.stdout.write(f"Deleted migration directory: {filename}")
                else:
                    os.remove(os.path.join(migration_path, filename))
                    self.stdout.write(f"Deleted migration file: {filename}")
                    
    def delete_processed_tickers(self):
        processed_tickers_path = os.path.join(settings.BASE_DIR, "processed_tickers.txt")
        if os.path.exists(processed_tickers_path):
            os.remove(processed_tickers_path)
            self.stdout.write("Deleted processed_tickers.txt")
        else:
            self.stdout.write("processed_tickers.txt not found. No deletion.")
            
    def delete_database(self):
        db_name = connection.settings_dict['NAME']
        if db_name:
            self.stdout.write(f"Deleting database: {db_name}")
            connection.close()
            time.sleep(2) 
            os.remove(db_name)
        else:
            self.stdout.write("Database not found. No deletion.")