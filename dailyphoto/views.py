

# 
import json
from json.decoder import JSONDecodeError
from django.http  import JsonResponse
from django.views import View
from time import time, timezone

from wsgiref.util import request_uri
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from dailyphoto.models import Profile
from django.contrib.auth import get_user_model
from .forms import PostForm, CustomUserChangeForm, ProfileForm, CommentForm
from .models import Post, Comment
from django.utils import timezone
from django.http import JsonResponse





# from PIL import Image

# 주소 index 
def index(request):
    """
    dailyphoto 게시물 출력
    """
    post_list = Post.objects.order_by('-create_date')

    context = {'post_list': post_list}
    return render(request, 'dailyphoto/post_list.html', context)

# post 상세
def detail(request, id):
    
    post  = get_object_or_404(Post, pk=id) # 예외일때 404에러 발생
    # get_object_or_404 <- 오류 화면 구성
    context = {'post': post}
    return render(request, 'dailyphoto/post_detail.html', context)
  

@login_required(login_url='common:login')
def comment_create(self, request):
    try :
        data = json.loads(request.body)
        user = request.user

        content    = data.get('content', None)
        post_id = data.get('post_id', None)

        if not (content and post_id):
            return JsonResponse({'message':'KEY_ERROR'}, status=400)

        if not Post.objects.filter(id=post_id).exists():
            return JsonResponse({'message':"POSTING_DOES_NOT_EXIST"}, status=404)
        
        posting = Post.objects.get(id=post_id)
        
        Comment.objects.create(
            content = content,
            user    = user,
            posting = posting
        )

        return JsonResponse({'message':'SUCCESS'}, status=200)
    
    except JSONDecodeError:
        return JsonResponse({'message':'JSON_DECODE_ERROR'}, status=400)


@login_required(login_url='common:login')
def comment_search(self, request, post_id,username):
    if not Post.objects.filter(id=post_id).exists():
        return JsonResponse({'message':'POSTING_DOES_NOT_EXIST'}, status=404)

    comment_list = [{
        "username"  : get_object_or_404(get_user_model(), username = username ),
        "content"   : comment.content,
        "create_at" : comment.created_date
        } for comment in Comment.objects.filter(post_id=post_id)
    ]

    return JsonResponse({'data':comment_list}, status=200)
      

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



#프로필화
def profile(request, username):
    person = get_object_or_404(get_user_model(), username = username )
    post_list = Post.objects.order_by('-create_date')
    post_photo = Post.objects.filter(author_id = request.user.id)
    
    
    context = {
      'post_list': post_list ,
       'person': person,
       'post_photo' : post_photo
       }

    return render(request, 'dailyphoto/profile.html', context)



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




