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
    
# def get_book_to_share_picture(request, ticker):
#     try:
#         book = plt.figure()
#         # plt.plot([1, 2, 3, 4])
#         # plt.ylabel('many numbers')
#         ticker = ticker.upper()
#         ticker_data = TickerData.objects.filter(ticker=ticker)
#         start_date = []
#         book_to_share_value = []
#         for data_point in ticker_data:
#             start_date.append(data_point.start_date)
#             book_to_share_value.append(data_point.book_to_share_value)
#         book.plot(start_date, book_to_share_value, label='book_to_share')
#         book.xlabel('Date')
#         book.ylabel('Book to Share Value Ratio')
#         book.title(f'{ticker.upper()}: Book to Share Value Over Time')
#         book.legend()
#         book.xticks(rotation=45, ha='right')

#         book.gcf().set_size_inches(20, 10)
        
#         book_to_share_buffer = io.BytesIO()
#         book.savefig(book_to_share_buffer, format='png')
#         book_to_share_buffer.seek(0)
#         book.close()
        
#         # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
#         return HttpResponse(book_to_share_buffer, content_type='image/png')
#     except TickerData.DoesNotExist:
#         return JsonResponse({'error': 'Ticker data not found'}, status=404)

# def get_current_ratio_picture(request, ticker):
#     try:
#         current= plt.figure()
#         # plt.plot([1, 2, 3, 4])
#         # plt.ylabel('many numbers')
#         ticker = ticker.upper()
#         ticker_data = TickerData.objects.filter(ticker=ticker)
#         start_date = []
#         current_ratio = []
#         for data_point in ticker_data:
#             start_date.append(data_point.start_date)
#             current_ratio.append(data_point.current_ratio)
#         current.plot(start_date, current_ratio, label='current_ratio')
#         current.xlabel('Date')
#         current.ylabel('Current Ratio')
#         current.title(f'{ticker.upper()}: Current Ratio Over Time')
#         current.legend()
#         current.xticks(rotation=45, ha='right')

#         current.gcf().set_size_inches(20, 10)
        
#         current_ratio_buffer = io.BytesIO()
#         current.savefig(current_ratio_buffer, format='png')
#         current_ratio_buffer.seek(0)
#         current.close()
        
#         # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
#         return HttpResponse(current_ratio_buffer, content_type='image/png')
#     except TickerData.DoesNotExist:
#         return JsonResponse({'error': 'Ticker data not found'}, status=404)

# def get_debt_ratio_picture(request, ticker):
#     try:
#         debt = plt.figure()
#         # plt.plot([1, 2, 3, 4])
#         # plt.ylabel('many numbers')
#         ticker = ticker.upper()
#         ticker_data = TickerData.objects.filter(ticker=ticker)
#         start_date = []
#         debt_ratio = []
#         for data_point in ticker_data:
#             start_date.append(data_point.start_date)
#             debt_ratio.append(data_point.debt_ratio)
#         debt.plot(start_date, debt_ratio, label='debt_ratio')
#         debt.xlabel('Date')
#         debt.ylabel('Debt Ratio')
#         debt.title(f'{ticker.upper()}: Debt Ratio Over Time')
#         debt.legend()
#         debt.xticks(rotation=45, ha='right')

#         debt.gcf().set_size_inches(20, 10)
        
#         debt_buffer = io.BytesIO()
#         debt.savefig(debt_buffer, format='png')
#         debt_buffer.seek(0)
#         debt.close()
        
#         # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
#         return HttpResponse(debt_buffer, content_type='image/png')
#     except TickerData.DoesNotExist:
#         return JsonResponse({'error': 'Ticker data not found'}, status=404)

# def get_dividend_yield_picture(request, ticker):
#     try:
#         dividend = plt.figure()
#         # plt.plot([1, 2, 3, 4])
#         # plt.ylabel('many numbers')
#         ticker = ticker.upper()
#         ticker_data = TickerData.objects.filter(ticker=ticker)
#         start_date = []
#         dividend_yield = []
#         for data_point in ticker_data:
#             start_date.append(data_point.start_date)
#             dividend_yield.append(data_point.dividend_yield)
#         dividend.plot(start_date, dividend_yield, label='dividend_yield_ratio')
#         dividend.xlabel('Date')
#         dividend.ylabel('Dividend Yield Ratio')
#         dividend.title(f'{ticker.upper()}: Dividend Yield Ratio Over Time')
#         dividend.legend()
#         dividend.xticks(rotation=45, ha='right')

#         dividend.gcf().set_size_inches(20, 10)
        
#         dividend_buffer = io.BytesIO()
#         dividend.savefig(dividend_buffer, format='png')
#         dividend_buffer.seek(0)
#         dividend.close()
        
#         # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
#         return HttpResponse(dividend_buffer, content_type='image/png')
#     except TickerData.DoesNotExist:
#         return JsonResponse({'error': 'Ticker data not found'}, status=404)

# def get_earnings_per_share_picture(request, ticker):
#     try:
#         earnings = plt.figure()
#         # plt.plot([1, 2, 3, 4])
#         # plt.ylabel('many numbers')
#         ticker = ticker.upper()
#         ticker_data = TickerData.objects.filter(ticker=ticker)
#         start_date = []
#         earnings_per_share = []
#         for data_point in ticker_data:
#             start_date.append(data_point.start_date)
#             earnings_per_share.append(data_point.earnings_per_share)
#         earnings.plot(start_date, earnings_per_share, label='dividend_yield_ratio')
#         earnings.xlabel('Date')
#         earnings.ylabel('Earnings Per Share')
#         earnings.title(f'{ticker.upper()}: Earnings Per Share Over Time')
#         earnings.legend()
#         earnings.xticks(rotation=45, ha='right')

#         earnings.gcf().set_size_inches(20, 10)
        
#         earnings_buffer = io.BytesIO()
#         earnings.savefig(earnings_buffer, format='png')
#         earnings_buffer.seek(0)
#         earnings.close()
        
#         # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
#         return HttpResponse(earnings_buffer, content_type='image/png')
#     except TickerData.DoesNotExist:
#         return JsonResponse({'error': 'Ticker data not found'}, status=404)

# def get_stock_prices_pictures(request, ticker):
#     try:
#         stock = plt.figure()
#         # plt.plot([1, 2, 3, 4])
#         # plt.ylabel('many numbers')
#         ticker = ticker.upper()
#         ticker_data = TickerData.objects.filter(ticker=ticker)
#         start_date = []
#         start_open = []
#         start_close = []
#         start_high = []
#         end_open = []
#         end_close = []
#         end_high = []
#         for data_point in ticker_data:
#             start_date.append(data_point.start_date)
#             start_open.append(data_point.start_open)
#             start_close.append(data_point.start_close)
#             start_high.append(data_point.start_high)
            
#             end_open.append(data_point.end_open)
#             end_close.append(data_point.end_close)
#             end_high.append(data_point.end_high)
#         stock.plot(start_date, start_open, label='start_open')
#         stock.plot(start_date, start_close, label='start_close')
#         stock.plot(start_date, start_high, label='start_high')
#         stock.plot(start_date, end_open, label='end_open')
#         stock.plot(start_date, end_close, label='end_close')
#         stock.plot(start_date, end_high, label='end_high')
#         stock.xlabel('Date')
#         stock.ylabel('Earnings Per Share')
#         stock.title(f'{ticker.upper()}: Earnings Per Share Over Time')
#         stock.legend()
#         stock.xticks(rotation=45, ha='right')

#         stock.gcf().set_size_inches(20, 10)
        
#         stock_buffer = io.BytesIO()
#         stock.savefig(stock_buffer, format='png')
#         stock_buffer.seek(0)
#         stock.close()
        
#         # return JsonResponse({'path': f"../stockdata/stockpictures/debt_ratio_picture/{ticker}.png"})
#         return HttpResponse(stock_buffer, content_type='image/png')
#     except TickerData.DoesNotExist:
#         return JsonResponse({'error': 'Ticker data not found'}, status=404)

def chart(request, ticker, chartname):
    try:
        plt.figure()
        ticker = ticker.upper()
        ticker_data = TickerData.objects.filter(ticker=ticker)
        start_date = []
        book_to_share_value = []
        dividend_yield = []
        current_ratio = []
        debt_ratio = []
        earnings_per_share = []
        start_open = []
        start_close = []
        start_high = []
        end_open = []
        end_close = []
        end_high = []
        for data_point in ticker_data:
            book_to_share_value.append(data_point.book_to_share_value)
            dividend_yield.append(data_point.dividend_yield)
            current_ratio.append(data_point.current_ratio)
            debt_ratio.append(data_point.debt_ratio)
            earnings_per_share.append(data_point.earnings_per_share)
            start_date.append(data_point.start_date)
            start_open.append(data_point.start_open)
            start_close.append(data_point.start_close)
            start_high.append(data_point.start_high)            
            end_open.append(data_point.end_open)
            end_close.append(data_point.end_close)
            end_high.append(data_point.end_high)
        if chartname == 'book_to_share':
            plt.plot(start_date, book_to_share_value, label='book_to_share')
#         book.xlabel('Date')
            plt.ylabel('Book to Share Value Ratio')
            plt.title(f'{ticker.upper()}: Book to Share Value Over Time')
        elif chartname == 'current_ratio':
            plt.plot(start_date, current_ratio, label='current_ratio')
            plt.ylabel('Current Ratio')
            plt.title(f'{ticker.upper()}: Current Ratio Over Time')
        elif chartname == 'debt_ratio':
            plt.plot(start_date, debt_ratio, label='debt_ratio')
            plt.ylabel('Debt Ratio')
            plt.title(f'{ticker.upper()}: Debt Ratio Over Time')
        elif chartname == 'dividend_yield':
            plt.plot(start_date, dividend_yield, label='dividend_yield_ratio')
            plt.ylabel('Dividend Yield Ratio')
            plt.title(f'{ticker.upper()}: Dividend Yield Ratio Over Time')
        elif chartname == 'earnings_per_share':
            plt.plot(start_date, earnings_per_share, label='dividend_yield_ratio')
            plt.ylabel('Earnings Per Share')
            plt.title(f'{ticker.upper()}: Earnings Per Share Over Time')
        elif chartname == 'stock_prices':
            plt.plot(start_date, start_open, label='start_open')
            plt.plot(start_date, start_close, label='start_close')
            plt.plot(start_date, start_high, label='start_high')
            plt.plot(start_date, end_open, label='end_open')
            plt.plot(start_date, end_close, label='end_close')
            plt.plot(start_date, end_high, label='end_high')
            
            plt.title(f'{ticker.upper()}: Earnings Per Share Over Time')
            plt.ylabel('Stocks Per Share')
        plt.xlabel('Date')
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