from django.shortcuts import render

# Create your views here.
import requests

def home(request):
    url = f'https://newsapi.org/v2/everything?q=tesla&from=2024-03-09&sortBy=publishedAt&apiKey=0dc7d12afaad4a53873b24d8e48fa0ce'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']

    context = {
        'articles':articles
    }
    return render(request,'news_api/home.html',context)
