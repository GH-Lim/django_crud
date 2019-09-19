from django.shortcuts import render, redirect
from .models import Article

# articles 의 메인 페이지, article list 를 보여줌
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# Variable Routing 으로 사용자가 보기를 원하는 페이지 pk 를 받아서 Detial 페이지를 보여줌
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 입력 페이지 제공
def new(request):
    return render(request, 'articles/new.html')

# 데이터를 전달 받아서 article 생성
def create(request):
    # /articles/new/ 에서 받은
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article()
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')
