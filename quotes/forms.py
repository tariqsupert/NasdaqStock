from django import forms
from .models import Tickers

class StockForm(forms.ModelForm):
    class Meta:
        model = Tickers
        fields = ["ticker"]