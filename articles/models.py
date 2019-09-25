from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    # on_delete=models.CASCADE ==> 'Article 이 삭제되면 Comment 도 같이 삭제'
    # comment.article ? => models.ForeignKey
    # article.comments ? => related_name == 'Article instance 가 comment 를 역참조 할 수 있는 이름을 정의'
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content
    