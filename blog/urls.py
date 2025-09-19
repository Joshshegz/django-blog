from django.urls import path
from . import views
# from .views import Posts, Post, PostUpdate, PostDelete, PostCreate, all_post, post_detail

# urlpatterns = [
#     path('posts/', Posts.as_view(), name = 'all_posts'),
#     path('post/<int:id>/', Post.as_view(), name = 'post_detail'),
#     path('post/<int:id>/edit/', PostUpdate.as_view(), name='post_update'), 
#     path('post/<int:id>/delete/', PostDelete.as_view(), name='post_delete'),
#     path('post/create/', PostCreate.as_view(), name='post_create'),
# ]

#url patterns for function based views
urlpatterns = [
    path('', views.all_post, name = 'all_posts'),
    path('post/<int:id>/', views.post_detail, name = 'post_detail'),
    ]