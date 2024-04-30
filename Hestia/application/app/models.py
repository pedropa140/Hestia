from django.db import models

class CompanyTicker(models.Model):
    company_name = models.CharField(max_length=100, default='Unknown')
    ticker = models.CharField(max_length=4, default='TICK', primary_key=True)

    def __str__(self):
        return f'{self.company} ({self.tick})'
    
class TickerData(models.Model):
    ticker = models.ForeignKey(CompanyTicker, related_name='ticker_data', default='TICK', on_delete=models.CASCADE)
    company_name = models.ForeignKey(CompanyTicker, related_name='company_data', default='Unknown', on_delete=models.CASCADE)
    start_date = models.DateField(default='1900-01-01', primary_key=True)
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
