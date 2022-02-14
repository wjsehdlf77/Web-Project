
from django.urls import path

from . import views


app_name = 'dailyphoto'


urlpatterns = [

    path('', views.index, name = "index"),
    path('detail/<int:post_id>/', views.detail, name="detail"), # <int:post_id>/   <- 상세보기 주소
    path('upload/', views.post_create, name="post_create"),
    path('profile/<str:username>/', views.profile, name="profile"),
    path('modify', views.modify_profile, name="modify_profile"),
    path('/comment', views.comment_create, name="comment_create"),
    path('/comment/search/<int:posting_id>', views.comment_search, name="comment_search"),
]


