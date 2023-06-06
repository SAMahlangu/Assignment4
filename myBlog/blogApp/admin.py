from django.contrib import admin
from blogApp.models import Post
from .models import Article,Topic
# Register your models here.
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Post)