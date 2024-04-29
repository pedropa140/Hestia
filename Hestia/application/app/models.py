from django.db import models


# class TickerData(models.Model):
#     # Define your TickerData model fields here
#     ticker_symbol = models.CharField(max_length=10)
#     company_name = models.CharField(max_length=100)
#     # Add more fields as needed
    
# TODO: Add actual TickerData fields
class TickerData(models.Model):
    # Define your TickerData model fields here
    company_name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=4)
    # Add more fields as needed
    book_value = models.FloatField()
    book_to_share_value = models.FloatField()
    earning_per_share = models.FloatField()
    debt_ratio = models.FloatField()
    current_ratio = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_open = models.FloatField()
    start_close = models.FloatField()
    start_high = models.FloatField()
    start_low = models.FloatField()
    end_open = models.FloatField()
    end_close = models.FloatField()
    end_high = models.FloatField()
    end_low = models.FloatField()
    

