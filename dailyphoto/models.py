

from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    subject = models.CharField(max_length = 200)    #varchar(200)이란뜻
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    #pk는 디폴트값으로 id Auto_increment  로 사용중 Question의 참조클라스가 id
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    modify_date = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return self.content

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True,
                                on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True,
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content