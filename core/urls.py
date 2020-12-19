from django.urls import path
from .views import *

urlpatterns = [
    path('', apiRouteList, name='api-detail'),

    path('profiles/', ProfileList.as_view(), name='profile-list'),
    path('profiles/<int:pk>', ProfileDetail.as_view(), name='profile-detail'),

    path('profile-posts/', PostList.as_view(), name='post-list'),
    path('profile-posts/<int:userId>', ProfilePostList.as_view(), name='profile-post-list'),

    path('posts-comments/', CommentList.as_view(), name='comment-list'),
    path('posts-comments/<int:pk>', CommentDetail.as_view(), name='comment-detail'),

    path('posts/<int:postId>/comments', CommentPostList.as_view(), name='comment-post-list'),
    path('posts/<int:postId>/comments/<int:pk>', CommentPostDetail.as_view(), name='comment-post-detail'),

    path('comments-post-user/', commentPostUserList, name='comment-post-user-detail'),
    path('comments-post-user/<int:pk>', commentPostUserDetail, name='comment-post-user-detail'),
]
