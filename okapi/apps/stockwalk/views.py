import datetime
from okapi.apps.stockwalk.models import Company
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {
        'companies': Company.objects.all(),
        })

def company(request, symbol):
    c = Company.objects.get(symbol=symbol)
    return render(request, 'company.html', {
        'symbol': symbol,
        'company': c,
        })
