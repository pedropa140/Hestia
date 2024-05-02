import os
from django.conf import settings
from django.shortcuts import render
from django.views import View
from .models import CompanyTicker, TickerData
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def indexHelp(request):

    # Pass the context along with the template
    return render(request, "help.html")

def indexAbout(request):

    # Pass the context along with the template
    return render(request, "about.html")

def indexMain(request):
    
    # Pass the context along with the template
    return render(request, "main.html")

def indexCompanies(request):
    companies_list = CompanyTicker.objects.all()

    # Check if a search query is present in the request
    search_query = request.GET.get('search_query')
    if search_query:
        # Process data for cosine similarity calculation
        corpus = [company.company_name for company in companies_list]
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(corpus)
        search_vector = vectorizer.transform([search_query])
        cosine_similarities = cosine_similarity(search_vector, X)
        top_indices = cosine_similarities.argsort()[0][::-1][:5]
        similar_companies = [companies_list[idx] for idx in top_indices]

        # Combine similar companies with pagination
        combined_list = list(similar_companies) + list(companies_list)
        paginator = Paginator(combined_list, 10)
    else:
        # Pagination logic without search query
        paginator = Paginator(companies_list, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj, 'search_query': search_query}
    return render(request, 'companies.html', context)

def indexCompany(request):
    return render(request, 'company.html')    

def indexDividend(request):
    
    # Pass the context along with the template
    return render(request, "dividend.html")

def get_company_tickers(request):
    company_tickers = CompanyTicker.objects.all()
    data = [{'ticker': ticker.ticker, 'company': ticker.company_name} for ticker in company_tickers]
    print("HELLO")
    return JsonResponse(data, safe=False)

def get_ticker_data(request, ticker):
    try:
        ticker = ticker.upper()
        ticker_data = TickerData.objects.filter(ticker=ticker)
        data = []
        for data_point in ticker_data:
            data.append({
                'ticker': data_point.ticker,
                'company_name': data_point.company_name,
                'start_date': data_point.start_date.strftime('%Y-%m-%d'),
                'end_date': data_point.end_date.strftime('%Y-%m-%d'),
                'book_value': data_point.book_value,
                'book_to_share': data_point.book_to_share_value,
                'earnings_per_share': data_point.earnings_per_share,
                'debt_ratio': data_point.debt_ratio,
                'current_ratio': data_point.current_ratio,
                'dividend_yield': data_point.dividend_yield,
                'start_open': data_point.start_open,
                'start_high': data_point.start_high,
                'start_close': data_point.start_close,
                'end_open': data_point.end_open,
                'end_close': data_point.end_close,
                'end_high': data_point.end_high,
            })
        return JsonResponse(data, safe=False)
    except TickerData.DoesNotExist:
        return JsonResponse({'error': 'Ticker data not found'}, status=404)

class DownloadCSV(View):
    def get(self, request, ticker):
        ticker = ticker.upper()
        file_path = os.path.join(settings.BASE_DIR, '../stockdata/div_info', f'{ticker}.csv')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as csv_file:
                response = HttpResponse(csv_file.read(), content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{ticker}.csv"'
                return response
        else:
            return HttpResponse('CSV file not found', status=404)