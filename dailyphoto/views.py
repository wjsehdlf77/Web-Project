from time import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from .forms import PostForm

from PIL import Image



# Create your views here.

# @login_required(login_url='common:login')
def post_create(request):
  """
  upload
  """
  if request.method== "POST":
    print('request method is post')
    form = PostForm(request.POST)
    # print(form)
    if form.is_valid():
      post = form.save(commit=False)
      print('post made')
      print(request.user)
      post.author= request.user
      post.create_date=timezone.now()
      post.save()
      print('save made?')
      return redirect('common/login.html')
    else:
      print('form is not valid')
  else:
    print('request method is not post')
    form=PostForm()
  context = {'form': form}
  return render(request, 'dailyphoto/upload_page.html', context)