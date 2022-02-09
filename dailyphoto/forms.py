
from django import forms
from dailyphoto.models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=['title',    'photo',    'content']
    widgets = { 'title': forms.TextInput(attrs={'class': 'form-control'}), 
    # 'photo': forms.ImageField(),
    # "Number" : forms.NumberInput(),
    'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),}
    labels = {
    'title': '제목',
    'photo':'사진',
    'content': '내용',
    }
