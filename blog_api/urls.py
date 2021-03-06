from django.urls import path
from rest_framework import urlpatterns
from .views import PostList, PostDetailBySlug, PostSearch, CreatePost, PostDetail, EditPost, DeletePost
from rest_framework.routers import DefaultRouter


app_name = "blog_api"

urlpatterns = [
    path('', PostList.as_view(), name="listposts"),
    path('post/<str:pk>/', PostDetailBySlug.as_view(), name="detailpost"),
    path('search/', PostSearch.as_view(), name='postsearch'),
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/postdetail/<int:pk>/',
         PostDetail.as_view(), name="admindetailpost"),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name="editpost"),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost')
]
