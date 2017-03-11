import datetime
from ewalk.models import Quote
from django.shortcuts import render

def index(request):
    q = Quote.objects.all()
    return render(request, 'home.html', {'quotes': q})
