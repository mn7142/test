from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.order_by('-created_at')[:2]
    return render(request , 'index.html' , {
        'title' : 'Articles Page',
        'articles' : articles,
        'mydata' : 24.2425,
    })

def single(request , article_id):
    article = Article.objects.get(id= article_id)
    return render(request , 'single.html' , {
        'title' : article.title ,
        'article' : article
    })