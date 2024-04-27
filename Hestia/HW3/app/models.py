from django.db import models

class TickerData(models.Model):
	ticker = models.CharField(max_length=4)
	date = models.BigIntegerField(primary_key=True)
	openprice = models.FloatField()
	closeprice = models.FloatField()
	high = models.FloatField()
	low = models.FloatField()
	volume = models.FloatField()

		
