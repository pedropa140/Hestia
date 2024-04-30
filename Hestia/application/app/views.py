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
    return JsonResponse(data, safe=False)

def get_ticker_data(request, ticker):
    try:
        ticker_data = TickerData.objects.get(ticker=ticker)
        data = {
            'ticker': ticker_data.ticker,
            'company_name': ticker_data.company_name,
            'start_date': ticker_data.start_date.strftime('%Y-%m-%d'),
            'end_date': ticker_data.end_date.strftime('%Y-%m-%d'),
            'book_value': ticker_data.book_value,
            'book_to_share_value': ticker_data.book_to_share_value,
            'earnings_per_share': ticker_data.earnings_per_share,
            'debt_ratio': ticker_data.debt_ratio,
            'current_ratio': ticker_data.current_ratio,
            'end_open': ticker_data.end_open,
            'dividend_yield': ticker_data.dividend_yield,
            'start_open': ticker_data.start_open,
            'start_close': ticker_data.start_close,
            'start_high': ticker_data.start_high,
            'start_low': ticker_data.start_low,
            'end_close': ticker_data.end_close,
            'end_high': ticker_data.end_high,
            'end_low': ticker_data.end_low,
            'volume': ticker_data.volume,
        }
        return JsonResponse(data)
    except TickerData.DoesNotExist:
        return JsonResponse({'error': 'Ticker data not found'}, status=404)

class DownloadCSV(View):
    def get(self, request, ticker):
        
        file_path = os.path.join(settings.BASE_DIR, '../../stockdata/div_info', f'{ticker}.csv')
        if os.path.exists(file_path):
            with open(file_path, 'rb') as csv_file:
                response = HttpResponse(csv_file.read(), content_type='text/csv')
                response['Content-Disposition'] = f'attachment; filename="{ticker}.csv"'
                return response
        else:
            return HttpResponse('CSV file not found', status=404)