
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



app_name = 'dailyphoto'



urlpatterns = [
    path('<str:username>/', views.dailyphoto_preview, name="dailyphoto_preview"),
    path('upload/', views.post_create, name="post_create"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

