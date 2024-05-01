import subprocess
import time
from django.apps import apps
from django.core.management.base import BaseCommand
from django.db import connection

from app.models import CompanyTicker, TickerData

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            # Run makemigrations for app
            self.stdout.write("Running makemigrations...")
            subprocess.run(["python", "manage.py", "makemigrations", "app"])
            
            # Run migrate
            self.stdout.write("Running migrate...")
            subprocess.run(["python", "manage.py", "migrate"])
            
            self.stdout.write("Checking if the database exists...")

            # Check if the default database connection is established and usable
            if connection.is_usable():
                # Check if CompanyTicker or TickerData models exist in the database
                if CompanyTicker.objects.exists() or TickerData.objects.exists():
                    confirm = input("CompanyTicker or TickerData models exist in the database. Do you want to overwrite them? [DELETES EXISTING DATABASE] (yes/no): ")
                    if confirm.lower() != 'yes':
                        self.stdout.write("Exiting setup. No changes were made.")
                        return
                    else:
                        self.stdout.write("Deleting the existing database...")
                        connection.close()
                        subprocess.run(["python", "manage.py", "delete_db"])
                        # Run makemigrations for app
                        self.stdout.write("Running makemigrations...")
                        subprocess.run(["python", "manage.py", "makemigrations", "app"])
                        # Run migrate
                        self.stdout.write("Running migrate...")
                        subprocess.run(["python", "manage.py", "migrate"])
                else:
                    self.stdout.write("No CompanyTicker or TickerData models found in the database.")
            else:
                self.stdout.write("Database connection not usable.")

            self.stdout.write("Setting up the database...")

            # Run populate_companies command
            self.stdout.write("Running populate_companies...")
            subprocess.run(["python", "manage.py", "populate_companies"])
            
            # Run process_csv_files command
            self.stdout.write("Running process_csv_files...")
            subprocess.run(["python", "manage.py", "process_csv_files"])

            self.stdout.write(self.style.SUCCESS("Database setup completed."))
        except KeyboardInterrupt:
            self.stdout.write("Interrupted by user. Exiting setup.")
        except:
            self.stdout.write(self.style.ERROR("An error occurred during database setup."))
            raise
