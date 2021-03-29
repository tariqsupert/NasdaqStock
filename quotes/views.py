from django.shortcuts import render,redirect
from .models import Tickers
from .forms import StockForm
from django.contrib import messages
# efe279573f74b7ef827f9f52f696376a account no.
# pk_578314fa031149afabb112f6e4e3e7e2  api token
# Create your views here.
def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_578314fa031149afabb112f6e4e3e7e2")
    
        try:
            api = json.loads(api_request.content)

        except Exception as e:
            api="There is an error. See the error message"
        return render(request, 'home.html',{'api': api})
    
    
    else:
        return render(request, 'home.html', {'ticker': "Please enter a valid ticker"})

    
    #api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/batch?types=quote&token=pk_578314fa031149afabb112f6e4e3e7e2")
    #api_request = requests.get("https://cloud.iexapis.com/stable/stock/market/batch?symbols=aapl,fb&types=quote&token=pk_578314fa031149afabb112f6e4e3e7e2")
    

def about(request):
    
    return render(request, 'about.html', {})

def delete(request):
    
    return render(request, 'delete.html', {})

def tickerDB(request):
    import requests
    import json
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,("Ticker has been added"))
            return redirect('tickerDB')
    else:    
        ticker = Tickers.objects.all()
        api_Output=[]
        for ticker_item in ticker:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote?token=pk_578314fa031149afabb112f6e4e3e7e2")
            
            try:
                api = json.loads(api_request.content)
                api_Output.append(api)
            except Exception as e:
                api="There is an error. See the error message"
       
    
        return render(request, 'tickerDB.html', {'ticker': ticker, 'api_Output':api_Output })

def deleteDB(request,ticker_id):
    item = Tickers.objects.get(pk=ticker_id)
    item.delete()
    messages.success(request,("Stock has been deleted"))
    return redirect(tickerDB)
"""
def delete_db(request, pk):
    order= Tickers.objects.get(pk=ticker_id)
    if request.method == "POST":
        order.delete()
        return redirect('tickerDB')
    

    context={'item':order}
    return render(request, 'delete.html', context)"""









