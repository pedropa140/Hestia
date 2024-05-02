import os
from django.conf import settings
from django.shortcuts import render
from django.views import View
from .models import CompanyTicker, TickerData
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import io
import base64

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
                'start_close': data_point.start_close,
                'start_high': data_point.start_high,
                'end_open': data_point.end_open,
                'end_close': data_point.end_close,
                'end_high': data_point.end_high,
            })
        return JsonResponse(data, safe=False)
    except TickerData.DoesNotExist:
        return JsonResponse({'error': 'Ticker data not found'}, status=404)
    
def get_book_to_share_picture(request, ticker):
    try:
        plt.figure()
        # plt.plot([1, 2, 3, 4])
        # plt.ylabel('many numbers')
        ticker = ticker.upper()
        ticker_data = TickerData.objects.filter(ticker=ticker)
        plt.figure()
        start_date = []
        book_to_share_value = []
        for data_point in ticker_data:
            start_date.append(data_point.start_date)
            book_to_share_value.append(data_point.book_to_share_value)
        plt.plot(start_date, book_to_share_value, label='dividend_yield_ratio')
        plt.xlabel('Date')
        plt.ylabel('Book to Share Value Ratio')
        plt.title(f'{ticker.upper()}: Book to Share Value Over Time')
        plt.legend()
        plt.xticks(rotation=45, ha='right')

        plt.gcf().set_size_inches(20, 10)
        
        book_to_share_buffer = io.BytesIO()
        plt.savefig(book_to_share_buffer, format='png')
        book_to_share_buffer.seek(0)
        plt.close()
        
        # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
        return HttpResponse(book_to_share_buffer, content_type='image/png')
    except TickerData.DoesNotExist:
        return JsonResponse({'error': 'Ticker data not found'}, status=404)

def get_current_ratio_picture(request, ticker):
    try:
        plt.figure()
        # plt.plot([1, 2, 3, 4])
        # plt.ylabel('many numbers')
        ticker = ticker.upper()
        ticker_data = TickerData.objects.filter(ticker=ticker)
        plt.figure()
        start_date = []
        current_ratio = []
        for data_point in ticker_data:
            start_date.append(data_point.start_date)
            current_ratio.append(data_point.current_ratio)
        plt.plot(start_date, current_ratio, label='dividend_yield_ratio')
        plt.xlabel('Date')
        plt.ylabel('Current Ratio')
        plt.title(f'{ticker.upper()}: Current Ratio Over Time')
        plt.legend()
        plt.xticks(rotation=45, ha='right')

        plt.gcf().set_size_inches(20, 10)
        
        current_ratio_buffer = io.BytesIO()
        plt.savefig(current_ratio_buffer, format='png')
        current_ratio_buffer.seek(0)
        plt.close()
        
        # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
        return HttpResponse(current_ratio_buffer, content_type='image/png')
    except TickerData.DoesNotExist:
        return JsonResponse({'error': 'Ticker data not found'}, status=404)

def get_debt_ratio_picture(request, ticker):
    try:
        plt.figure()
        # plt.plot([1, 2, 3, 4])
        # plt.ylabel('many numbers')
        ticker = ticker.upper()
        ticker_data = TickerData.objects.filter(ticker=ticker)
        plt.figure()
        start_date = []
        debt_ratio = []
        for data_point in ticker_data:
            start_date.append(data_point.start_date)
            debt_ratio.append(data_point.debt_ratio)
        plt.plot(start_date, debt_ratio, label='dividend_yield_ratio')
        plt.xlabel('Date')
        plt.ylabel('Debt Ratio')
        plt.title(f'{ticker.upper()}: Debt Ratio Over Time')
        plt.legend()
        plt.xticks(rotation=45, ha='right')

        plt.gcf().set_size_inches(20, 10)
        
        debt_buffer = io.BytesIO()
        plt.savefig(debt_buffer, format='png')
        debt_buffer.seek(0)
        plt.close()
        
        # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
        return HttpResponse(debt_buffer, content_type='image/png')
    except TickerData.DoesNotExist:
        return JsonResponse({'error': 'Ticker data not found'}, status=404)

def get_dividend_yield_picture(request, ticker):
    try:
        plt.figure()
        # plt.plot([1, 2, 3, 4])
        # plt.ylabel('many numbers')
        ticker = ticker.upper()
        ticker_data = TickerData.objects.filter(ticker=ticker)
        plt.figure()
        start_date = []
        dividend_yield = []
        for data_point in ticker_data:
            start_date.append(data_point.start_date)
            dividend_yield.append(data_point.dividend_yield)
        plt.plot(start_date, dividend_yield, label='dividend_yield_ratio')
        plt.xlabel('Date')
        plt.ylabel('Dividend Yield Ratio')
        plt.title(f'{ticker.upper()}: Dividend Yield Ratio Over Time')
        plt.legend()
        plt.xticks(rotation=45, ha='right')

        plt.gcf().set_size_inches(20, 10)
        
        dividend_buffer = io.BytesIO()
        plt.savefig(dividend_buffer, format='png')
        dividend_buffer.seek(0)
        plt.close()
        
        # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
        return HttpResponse(dividend_buffer, content_type='image/png')
    except TickerData.DoesNotExist:
        return JsonResponse({'error': 'Ticker data not found'}, status=404)

def get_earnings_per_share_picture(request, ticker):
    try:
        plt.figure()
        # plt.plot([1, 2, 3, 4])
        # plt.ylabel('many numbers')
        ticker = ticker.upper()
        ticker_data = TickerData.objects.filter(ticker=ticker)
        plt.figure()
        start_date = []
        earnings_per_share = []
        for data_point in ticker_data:
            start_date.append(data_point.start_date)
            earnings_per_share.append(data_point.earnings_per_share)
        plt.plot(start_date, earnings_per_share, label='dividend_yield_ratio')
        plt.xlabel('Date')
        plt.ylabel('Earnings Per Share')
        plt.title(f'{ticker.upper()}: Earnings Per Share Over Time')
        plt.legend()
        plt.xticks(rotation=45, ha='right')

        plt.gcf().set_size_inches(20, 10)
        
        earnings_buffer = io.BytesIO()
        plt.savefig(earnings_buffer, format='png')
        earnings_buffer.seek(0)
        plt.close()
        
        # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
        return HttpResponse(earnings_buffer, content_type='image/png')
    except TickerData.DoesNotExist:
        return JsonResponse({'error': 'Ticker data not found'}, status=404)

def get_stock_prices_pictures(request, ticker):
    try:
        plt.figure()
        # plt.plot([1, 2, 3, 4])
        # plt.ylabel('many numbers')
        ticker = ticker.upper()
        ticker_data = TickerData.objects.filter(ticker=ticker)
        plt.figure()
        start_date = []
        start_open = []
        start_close = []
        start_high = []
        end_open = []
        end_close = []
        end_high = []
        for data_point in ticker_data:
            start_date.append(data_point.start_date)
            start_open.append(data_point.start_open)
            start_close.append(data_point.start_close)
            start_high.append(data_point.start_high)
            
            end_open.append(data_point.end_open)
            end_close.append(data_point.end_close)
            end_high.append(data_point.end_high)
        plt.plot(start_date, start_open, label='start_open')
        plt.plot(start_date, start_close, label='start_close')
        plt.plot(start_date, start_high, label='start_high')
        plt.plot(start_date, end_open, label='end_open')
        plt.plot(start_date, end_close, label='end_close')
        plt.plot(start_date, end_high, label='end_high')
        plt.xlabel('Date')
        plt.ylabel('Earnings Per Share')
        plt.title(f'{ticker.upper()}: Earnings Per Share Over Time')
        plt.legend()
        plt.xticks(rotation=45, ha='right')

        plt.gcf().set_size_inches(20, 10)
        
        stock_buffer = io.BytesIO()
        plt.savefig(stock_buffer, format='png')
        stock_buffer.seek(0)
        plt.close()
        
        # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
        return HttpResponse(stock_buffer, content_type='image/png')
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