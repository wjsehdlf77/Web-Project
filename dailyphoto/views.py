
import json
from json.decoder import JSONDecodeError
from django.http  import JsonResponse , HttpResponse
from django.views import View

from time import time, timezone

from wsgiref.util import request_uri
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth import get_user_model



from .forms import LikeForm, PostForm, CustomUserChangeForm, ProfileForm, CommentForm
from .models import Post, Comment, Profile, Like
from . import models
from django.utils import timezone
from django.http import JsonResponse
from django.urls import reverse


# from PIL import Image

# 주소 index 
def index(request):
    """
    dailyphoto 게시물 출력
    """
    
 
    post_list = Post.objects.order_by('-create_date')
    comment_form = CommentForm

    like_list = []
    like_my = Like.objects.filter(author=request.user)
    for a_post in post_list:
      print(a_post)
      is_liked = like_my.filter(post = a_post)
      print(is_liked)
      print(is_liked.count())
      if(is_liked.count()):
        like_list.append(True)
      else:
        like_list.append(False)
    print(like_list)

    context = {'post_list': post_list,  "comment_form" : comment_form ,'like_list':like_list}
    return render(request, 'dailyphoto/post_list.html', context)

# post 상세
def detail(request, id):
    
    post  = get_object_or_404(Post, pk=id) # 예외일때 404에러 발생
    # get_object_or_404 <- 오류 화면 구성
    context = {'post': post}
    return render(request, 'dailyphoto/post_detail.html', context)
  

@login_required(login_url='common:login')
def comment_create(request, post_id):
      if request.user.is_authenticated:

            post = get_object_or_404(models.Post, pk=post_id)

            form = CommentForm(request.POST)
            if form.is_valid():
                  comment = form.save(commit=False)
                  comment.author = request.user
                  comment.post = post
                  comment.save()
                  
                  return redirect(reverse('dailyphoto:index')+"#comment-"+str(comment.id))

            else:
                  return render(request, 'dailyphoto/post_list.html')
                  

def comment_delete(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(models.Comment, pk=comment_id)
        if request.user == comment.author:
            comment.delete()

        return redirect(reverse('posts:index'))

    else:
        return render(request, 'dailyphoto/post_list.html')
      

# 글 업로드 함수
# @login_required(login_url='common:login')
def post_create(request): 
  """
  upload
  """

  if request.method== "POST":
    print('request method is post')
    print(request.POST)
    form = PostForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)  

      # title이 입력되지 않으면 현재날짜를 title로 넣어줌
      if post.title == None:
        post.title=timezone.localdate()

      # photo가 입력되었는지 확인하고 넣어줌
      if 'photo' in request.FILES:
        post.photo=request.FILES['photo']
      else:
        pass

      # 리스트로 입력된 icons를 스트링으로 변환해서 필드에 넣어줌
      icons = request.POST.getlist('icons[]')
      post.icons='&'.join(icons)

      post.author= request.user
      post.create_date=timezone.now()
      post.save()
      print('post save made')
      return redirect('dailyphoto:index')

    else:
      print('form is not valid')

  else:
    print('request method is get')
    form=PostForm()
    
  context = {'form': form }
  return render(request, 'dailyphoto/upload_page.html', context )


#like
@login_required(login_url='common:login')
def like(request):

  def liking(post, like,like_count):
    like.post=post
    post.like_count = like_count + 1
    print(like)
    like.save()
    post.save()
    print('liked')

  if request.method=="POST":
    form = LikeForm(request.POST)
    
    print(request.body)
    if form.is_valid():
      like=form.save(commit=False)
      like.author= request.user
      data=request.body.decode()
      data = data.split('&')
      data_post=data[0].split('=')[1]
      post = get_object_or_404(models.Post, pk=data_post)
      post_filtered = Like.objects.filter(post_id = data_post)
      if post_filtered:
        user_filtered = post_filtered.filter(author_id=request.user)
        if user_filtered :
          print('double liking error')
        else:
          like_count=post_filtered.count()
          liking(post,like,like_count)
      else:
        like_count=post_filtered.count()
        liking(post,like,like_count)
    else:
      print('form is not valid')
  else:
    print('else')
    print(request)

  return HttpResponse()

# like 취소
@login_required(login_url='common:login')
def unlike(request):

  if request.method=="POST":
    form = LikeForm(request.POST)
    
    print(request.body)
    if form.is_valid():
      data=request.body.decode()
      data = data.split('&')
      data_post=data[0].split('=')[1]
      post = get_object_or_404(models.Post, pk=data_post)
      post_filtered = Like.objects.filter(post_id = data_post)
      if post_filtered:
        user_filtered = post_filtered.filter(author_id=request.user)
        if user_filtered :
          print('like data exist')
          like = user_filtered.first()
          print(like)
          like.delete()
          post.like_count = post_filtered.count() -1
          post.save()
        else:
          pass
      else:
        pass
    else:
      print('form is not valid')
  else:
    print('else')
    print(request)

  return HttpResponse()

# def show_like(request):
#   if request.method=="GET":
#     print('showlike 함수 시작')
#     print(request.body)
#     data=request.body.decode()
#     print(data)
#     data = data.split('&')
#     data_post=data[0].split('=')[1]
#     print(data_post)
#     post = get_object_or_404(models.Post, pk=data_post)
#     post_filtered = Like.objects.filter(post_id = data_post)
#     if post_filtered:
#       user_filtered = post_filtered.filter(author_id=request.user)
#       if user_filtered :
#         print('like data exist')
#         # like = user_filtered.first()
#         data = {
#           'like':True 
#         }
#       # return JsonResponse(data)
#         return data
#         return True 

#   else:
#     pass

#   return HttpResponse()



#프로필화
def profile(request, username):
    person = get_object_or_404(get_user_model(), username = username )
    post_photo = Post.objects.filter(author_id = person.id).order_by('-create_date')

    context = {
       'person': person,
       'post_photo' : post_photo
       }
    # url='dailyphoto/profile/'+username+'.html'
    url='dailyphoto/profile.html'
    print(url)

    return render(request, url, context)



def modify_profile(request):
    if request.method == 'POST':
      user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
      profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
      if user_change_form.is_valid() and profile_form.is_valid():
          user = user_change_form.save()
          profile_form.save()
          return redirect('dailyphoto:profile', user.username)
      return redirect('dailyphoto:profile')
    else:
        user_change_form = CustomUserChangeForm(instance=request.user)
        profile, create = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(instance=profile)
        return render(request, 'dailyphoto/profile_form.html', {
            'user_change_form': user_change_form,
            'profile_form': profile_form
        })




def follow(request, user_id):
  if request.user.is_authenicated:
    follow_user = get_object_or_404(get_user_model(), pk = user_id)
    if follow_user != request.user:
      if follow_user.followers.filter(pk = request.user.id).exists():
        follow_user.followers.remove(request.user)
      else:
        follow_user.followers.add(request.user)
      return redirect('dailyphoto:profile', follow_user.username)
    return redirect('dailyphoto:login')





  



