

from django.db import models
from django.contrib.auth.models import User

# Bulletin : 게시글
class Post(models.Model):
    subject = models.CharField(max_length = 200)    #varchar(200)이란뜻
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.subject


# 댓글 
class Answer(models.Model):
    bulletin = models.ForeignKey(Post, on_delete=models.CASCADE)    #pk는 디폴트값으로 id Auto_increment  로 사용중 Question의 참조클라스가 id
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.content
