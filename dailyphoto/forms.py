
from django import forms
from dailyphoto.models import Post

from django.contrib.auth.forms import UserChangeForm
from dailyphoto.models import Profile
from django.contrib.auth import get_user_model




class PostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=['title','photo','content']
    widgets = { 'title': forms.TextInput(attrs={'class': 'form-control'}), 
    # 'photo': forms.ImageField(attrs={'class': 'form-control-file'}),
    'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),}
    labels = {
    'title': '제목',
    'photo':'사진',
    'content': '내용',
    }



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
