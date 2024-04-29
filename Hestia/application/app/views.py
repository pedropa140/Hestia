from django.shortcuts import render
from .models import TickerData
import json
from django.http import JsonResponse
def indexHelp(request):

    # Pass the context along with the template
    return render(request, "help.html")

def indexAbout(request):

    # Pass the context along with the template
    return render(request, "about.html")

def indexMain(request):
    
    # Pass the context along with the template
    return render(request, "main.html")

def indexDividend(request):
    
    # Pass the context along with the template
    return render(request, "dividend.html")

def indexMainData(request):
    print(TickerData.objects.values())
    return JsonResponse(list(TickerData.objects.values()), safe=False)


