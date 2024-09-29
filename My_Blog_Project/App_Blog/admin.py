from django.contrib import admin
from App_Blog.models import Blog, Likes, Comment, Category 

# Register your models here.
admin.site.register(Blog),
admin.site.register(Likes),
admin.site.register(Comment),
admin.site.register(Category)