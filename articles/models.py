from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()  # 문자열 빈 값 저장은 null 이 아니라 '' => null=True 를 사용하지 말자
    image = models.ImageField(blank=True, null=True)
    # black: 데이터 유효성과 관련되어있다 (True: 아무런 값이 넘어오지 않아도 저장 가능)
    # null: DB와 관련되어있다
    # blank vs null
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # comment.article ? => models.ForeignKey
    # on_delete=models.CASCADE ==> 'Article 이 삭제되면 Comment 도 같이 삭제'
    # article.comments ? => related_name == 'Article instance 가 comment 를 역참조 할 수 있는 이름을 정의'
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content
    