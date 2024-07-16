from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
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


@login_required
def update_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'update.html', {'form': form})

@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('home')
    return render(request, 'delete.html', {'article': article})

def add(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm()
    return render(request, 'add.html', {'form': form})



