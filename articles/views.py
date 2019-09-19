from django.shortcuts import render, redirect, get_object_or_404
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
    article = get_object_or_404(Article, pk=article_pk)  # pk 라는 인자를 넘겨줘야합니다!
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 입력 페이지 제공
# GET /articles/create
# def new(request):
#     return render(request, 'articles/new.html')

# 데이터를 전달 받아서 article 생성
# POST /articles/create
def create(request):
    # 만약 POST일 경우 사용자 데이터 받아서 article 생성
    if request.method == 'POST':
        title = request.POST.get('title')  # POST 요청으로 받아야합니다!
        content = request.POST.get('content')

        article = Article()
        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', article.pk)
        
    # GET 요청으로 들어오면 html 페이지 rendering
    else:
        return render(request, 'articles/create.html')

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 만약 POST 요청이라면 사용자 데이터 받아서 article 수정
    # POST /articles/#/update/
    if request.method == 'POST':
        title = request.POST.get('title')  # POST 요청으로 받아야합니다!
        content = request.POST.get('content')

        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', article.pk)
    # 아니라면 수정하는 페이지 rendering
    # GET /articles/#/update/ : update 하기위한 페이지 보여줌
    else:
        context = {
            'article': article
        }
        return render(request, 'articles/update.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article_pk)