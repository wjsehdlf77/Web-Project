
from dataclasses import field
from django import forms
from dailyphoto.models import Post

from django.contrib.auth.forms import UserChangeForm
from dailyphoto.models import Profile, Comment
from django.contrib.auth import get_user_model




class PostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=['title','photo','content','icons']
    widgets = { 'title': forms.TextInput(attrs={'class': 'form-control'}), 
    'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),}
    labels = {
    'title': '제목',
    'photo':'사진',
    'content': '내용',
    }

# class LikeForm(forms.ModelForm):
#   class Meta:
#     model=Post

class CommentForm(forms.ModelForm): 
    class Meta:
        model = Comment 
        fields = ['content'] 
        labels = {'content': '댓글내용', }

# class PostSerializer(serializers.ModelSerializer):
#       comment_post = CommentSerializer(many=True)
#       author = FeedAuthorserializer()
      
#       class Meta:
#             model = Post
#             fields = (
#               "id",
#               "image",
#               "caption",
#               "comment_post",
#               "author"
#             )
      








class CustomUserChangeForm(UserChangeForm):
  password = None
  class Meta:
        model = get_user_model()
        fields = ['email']
        
class ProfileForm(forms.ModelForm):
    nickname = forms.CharField(label="별명", required=False)
    description = forms.CharField(label="자기소개", required=False, widget=forms.Textarea())
    image = forms.ImageField(label="이미지", required=False)
    class Meta:
        model = Profile
        fields = ['nickname', 'description', 'image',]
