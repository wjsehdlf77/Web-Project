# from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import FileExtensionValidator


# 게시물 
class Post(models.Model):
    title = models.CharField(max_length = 200,blank=True,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='post_author')
    content = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="pic/",blank=True,null=True)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    like_count = models.IntegerField(default=0)
    icons=models.CharField(max_length=1000,default='',blank=True)

# 댓글    
class Comment(models.Model):
    author       = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    post       = models.ForeignKey('Post', on_delete=models.CASCADE)
    parent     = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    content    = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

# 좋아요
class Like(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

#프로필
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = models.ImageField(upload_to= 'image/', blank=True)   #Pillow설치
    music = models.FileField(upload_to= 'music/', blank = True, validators=[FileExtensionValidator(allowed_extensions=['mp3'])]) 

    def __str__(self):
        return self.nickname
        
#팔로우
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)

    def __str__(self):
        return self.followings








