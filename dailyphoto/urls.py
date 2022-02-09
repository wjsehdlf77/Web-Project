
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name = 'dailyphoto'


urlpatterns = [

    path('dailyphoto/', views.index),
    path('<int:post_id>/', views.detail), # <int:post_id>/   <- 상세보기 주소
    path('upload/', views.post_create, name="post_create"),
    path('<str:username>/', views.dailyphoto_preview, name="dailyphoto_preview"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


