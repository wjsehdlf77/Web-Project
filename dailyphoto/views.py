from django.shortcuts import render, get_object_or_404
from .models import Post
def index(request):
    """
    dailyphoto 게시물 출력
    """
    post_list = Post.objects.order_by('-create_date')
    context = {'form': post_list}
    
    return render(request, 'dailyphoto/post_list.html', context)

def detail(request, post_id):
    
    post  = get_object_or_404(Post, pk=post_id) # 예외일때 404에러 발생
    # get_object_or_404 <- 오류 화면 구성
    context = { 'post': post}
    return render(request, 'pybo/quesiton_detail.html', context)