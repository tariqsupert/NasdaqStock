from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tickers(models.Model):
    tickerowner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
        
        
    ticker = models.CharField(max_length=10) 

    def __str__(self):
        return self.ticker
    