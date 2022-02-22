from django.contrib import admin
from .models import Post,Comment,Like,Profile

class PostAdmin(admin.ModelAdmin):
  search_fields = ['title']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Profile)
# Register your models here.