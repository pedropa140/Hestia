from django.db import models

class CompanyTicker(models.Model):
    company_name = models.CharField(max_length=100, default='Unknown')
    ticker = models.CharField(max_length=6, default='TICK', primary_key=True)

    def __str__(self):
        return f'{self.company_name} ({self.ticker})'
    
class TickerData(models.Model):
    ticker = models.CharField(max_length=6, default='TICK')
    company_name = models.CharField(max_length=100, default='Unknown')
    start_date = models.DateField(default='1900-01-01')
    end_date = models.DateField(default='1900-01-01')
    book_value = models.FloatField(default=-1.0)
    book_to_share_value = models.FloatField(default=-1.0)
    earnings_per_share = models.FloatField(default=-1.0)
    debt_ratio = models.FloatField(default=-1.0)
    current_ratio = models.FloatField(default=-1.0)
    end_open = models.FloatField(default=-1.0)
    dividend_yield = models.FloatField(default=-1.0)
    start_open = models.FloatField(default=-1.0)
    start_close = models.FloatField(default=-1.0)
    start_high = models.FloatField(default=-1.0)
    start_low = models.FloatField(default=-1.0)
    end_close = models.FloatField(default=-1.0)
    end_high = models.FloatField(default=-1.0)
    end_low = models.FloatField(default=-1.0)
    volume = models.FloatField(default=-1.0)
    id = models.AutoField(primary_key=True)
