
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    photo = models.ImageField(upload_to="pic/",blank=True,null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    like_count = models.IntegerField(default=0)
    icon_emotion=models.CharField(max_length=20, default='happy')
    icon_weather=models.CharField(max_length=20, default='sunny')
    
    class Meta:
        db_table = 'posts'



    def __str__(self):
        return self.subject
    
class Comment(models.Model):
    author       = models.ForeignKey('user.User', on_delete=models.CASCADE)
    post       = models.ForeignKey('Post', on_delete=models.CASCADE)
    parent     = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    # 대댓글 구현을 위해 parent 추가
    content    = models.CharField(max_length=500)
    create_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
        
        
        
class PersonalIconSet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    emotion_is_setted=models.BooleanField(default=True)
    weather_is_setted=models.BooleanField(default=True)

    

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to= 'image/', blank=True)   #Pillow설치

    def __str__(self):
        return self.nickname





