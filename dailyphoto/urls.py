from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pots_id>/', views.detail), # <int:pots_id>/   <- 상세보기 주소
]