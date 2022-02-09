

# from time import timezone
from wsgiref.util import request_uri
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from dailyphoto.models import Profile

from django.contrib.auth import get_user_model
from .forms import PostForm
from .models import Post
from django.utils import timezone

# from PIL import Image

# 주소 index 
def index(request):
    """
    dailyphoto 게시물 출력
    """
    post_list = Post.objects.order_by('-create_date')
    context = {'form': post_list}
    
    return render(request, 'dailyphoto/post_list.html', context)

# post 상세
def detail(request, post_id):
    
    post  = get_object_or_404(Post, pk=post_id) # 예외일때 404에러 발생
    # get_object_or_404 <- 오류 화면 구성
    context = { 'post': post}
    return render(request, 'dailyphoto/post_detail.html', context)

# 글 업로드 함수
# @login_required(login_url='common:login')
def post_create(request): 
  """
  upload
  """
  if request.method== "POST":
    print('request method is post')
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      # print('post made')
      # print(request.user)
      # print(request)
      # print(form)
      post.photo=request.FILES['photo']
      post.author= request.user
      post.create_date=timezone.now()
      post.save()
      print('save made?')
      return redirect('dailyphoto:post_create')
    else:
      print('form is not valid')
  else:
    print('request method is not post its get')
    form=PostForm()
  context = {'form': form}
  return render(request, 'dailyphoto/upload_page.html', context)

#프로필화
def dailyphoto_preview(request, username): # 프로필
    person = get_object_or_404(get_user_model(), username=username)

    return render(request, 'dailyphoto/profile.html', {'person': person})

