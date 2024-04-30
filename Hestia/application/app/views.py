from django.shortcuts import render
from .models import CompanyTicker, TickerData
from django.core.paginator import Paginator
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

def indexCompany(request):
    companies_list = CompanyTicker.objects.all()
    paginator = Paginator(companies_list, 10)  # Show 10 companies per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'companies.html', {'page_obj': page_obj})


def indexDividend(request):
    
    # Pass the context along with the template
    return render(request, "dividend.html")


