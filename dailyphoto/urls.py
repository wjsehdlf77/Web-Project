
from django.urls import path

from . import views, apps

app_name = 'dailyphoto'


urlpatterns = [

    path('', views.index, name = "index"),
    path('detail/<int:id>/', views.detail, name="detail"), # <int:post_id>/   <- 상세보기 주소
  # 글 생성/수정/삭제
    path('upload/', views.post_create, name="post_create"),
    path('update/',views.post_update,name="post_update"),
    path('delete/',views.post_delete,name="post_delete"),
  # 팔로우
    path('<int:user_pk>/follow/', views.follow, name='follow'),
  # PROFILE
    path('profile/<str:username>/', views.profile, name="profile"),
  # Like
    path('modify/', views.modify_profile, name="modify_profile"),
    path('like/',views.like, name='like'),
    path('unlike/',views.unlike, name='unlike'),
  # COMMENT
    path('<int:post_id>/comment_create/' , views.comment_create, name="comment_create"),
    path('<int:comment_id>/comment_delete/', views.comment_delete, name="comment_delete"),

    


]
