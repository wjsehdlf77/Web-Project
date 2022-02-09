from django.contrib import admin
from django.urls import path, include
#from common import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.signup, name="signup"),
    path('', include('common.urls'),name='index'),
    path('dailyphoto/',include('dailyphoto.urls'))

]

