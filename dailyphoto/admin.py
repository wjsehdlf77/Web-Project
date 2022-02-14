from django.contrib import admin
from .models import Post, Answer

class PostAdmin(admin.ModelAdmin):
  search_fields = ['title']


admin.site.register(Post,PostAdmin)
admin.site.register(Answer)

# Register your models here.

