
from django.urls import path


from . import views


app_name = 'dailyphoto'


urlpatterns = [

    path('', views.index, name = "index"),
    path('<int:post_id>/', views.detail), # <int:post_id>/   <- 상세보기 주소
    path('upload/', views.post_create, name="post_create"),
    path('<str:username>/', views.profile, name="profile"),
    path('modify', views.modify_profile, name="modify_profile"),
]






