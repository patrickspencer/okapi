import datetime
from ewalk.models import Symbol, Quote
from django.shortcuts import render

def index(request):
    q = Quote.objects.all()
    s = Symbol.objects.all()
    return render(request, 'home.html', {
        'quotes': q,
        'symbols': s,
        })
