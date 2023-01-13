from django.urls import path
from server.apps.posts.views import posts_list, posts_create

urlpatterns = [
  path("", posts_list),
  path("posts/create", posts_create),
]