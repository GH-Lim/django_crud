from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment

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
    comments = article.comments.all()
    # related_name 이 설정 되면 comment_set.all() 을 사용할 수 없습니다.
    context = {
        'article': article,
        'comments': comments,
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

def comments_create(request, article_pk):
    # article_pk 에 해당하는 article 에 새로운 comment 생성
    # 생성한 다음 detail page 로 redirect
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment()
        comment.content = content
        comment.article = article  # 어떤 article 의 comment 인지 알려주기 위한 작업
        # comment.article_id = article_pk  # 위와 완전히 같은 기능의 코드
        comment.save()
    # GET 요청으로 들어오면 if 실행 안하고 redirect
    return redirect('articles:detail', article_pk)

def comments_delete(request, article_pk, comment_pk):
    # comment_pk 에 해당하는 댓글 삭제
    # 댓글 삭제 후 detail 페이지로 이동
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
    return redirect('articles:detail', article_pk)
