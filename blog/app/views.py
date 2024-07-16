from django.shortcuts import render, get_object_or_404,redirect
from .models import Article,Comment
from .forms import ArticleForm, CommentForm


def home(request):
    products = Article.objects.all()
    return render(request, 'home.html', {'products': products})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    })


def add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'addArt.html', {'form': form})



