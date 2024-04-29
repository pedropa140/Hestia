from django.db import models

class TickerData(models.Model):
    # Define your TickerData model fields here
    ticker_symbol = models.CharField(max_length=10)
    company_name = models.CharField(max_length=100)
    # Add more fields as needed
