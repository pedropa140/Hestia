from django.shortcuts import render
from .models import CompanyTicker, TickerData
from django.core.paginator import Paginator
from django.http import JsonResponse
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


