
from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User


class Post(models.Model):
    subject = models.CharField(max_length = 200)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    photo=models.ImageField(upload_to=None,null=True,blank=True)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # User모델과 Profile을 1:1로 연결
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(blank=True)   #Pillow설치

