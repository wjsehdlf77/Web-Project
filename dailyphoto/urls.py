
from django.urls import path
from . import views

app_name = 'dailyphoto'


urlpatterns = [
    path('', views.index, name = "index"),
    path('detail/<int:id>/', views.detail, name="detail"),
    
  # 글 생성/수정/삭제
    path('upload/', views.post_create, name="post_create"),
    path('update/<int:post_id>',views.post_update,name="post_update"),
    path('delete/<int:post_id>',views.post_delete,name="post_delete"),

  # 팔로우
    path('<int:user_pk>/follow/', views.follow, name='follow'),

  # PROFILE
    path('profile/<str:username>/', views.profile, name="profile"),
    path('modify/', views.modify_profile, name="modify_profile"),

  # Like
    path('like/',views.like, name='like'),
    path('unlike/',views.unlike, name='unlike'),
    
  # COMMENT
    path('<int:post_id>/comment_create/' , views.comment_create, name="comment_create"),
    path('<int:comment_id>/comment_delete/', views.comment_delete, name="comment_delete"),

  # search
    path('search/',views.search, name="search"),
    path('search/like/',views.like, name='like'),
    path('search/unlike/',views.unlike, name='unlike'),
]
