from django.urls import path
from App_Blog import views
app_name = 'App_Blog'
urlpatterns = [
    path('', views.blog_list, name="blog_list"),
    # path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<str:slug>/', views.blog_details, name="blog_details"),
    path('liked/<pk>', views.liked, name="liked_post"),
    path('unliked/<pk>', views.unliked, name="unliked_post"),
    path('my-blogs/', views.MyBlogs.as_view(), name="my_blogs"),
    path('edit/<pk>/', views.UpdateBlog.as_view(), name="edit_blog"),
    path('delete/<pk>/', views.DeletePost.as_view(), name="delete_blog"),
    path('categories/', views.CategoryList.as_view(), name='categories'),
    path('category-posts/<str:category>', views.ViewByCategory, name='category_posts')
]