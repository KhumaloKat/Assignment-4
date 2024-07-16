from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    products = Article.objects.all()
    return render(request, 'home.html', {'products': products})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})
