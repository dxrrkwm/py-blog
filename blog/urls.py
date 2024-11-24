from django.contrib import admin
from django.urls import path, include

from blog.views import IndexView, PostDetailView, comment

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/comment', comment, name='add-comment'),
]