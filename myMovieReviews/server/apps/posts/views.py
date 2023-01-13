from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from server.apps.posts.models import Post
# Create your views here.

def posts_list(request: HttpRequest, *args, **kwargs):
  posts = Post.objects.all()
  print({"posts": posts})
  return render(request, "posts/posts_list.html", {"posts": posts})

def posts_retrieve(request: HttpRequest, pk, *args, **kwargs):
  post = Post.objects.all().get(id=pk)
  print(post)
  return render(request, "posts/posts_retrieve.html", {"post":post})

def posts_create(request: HttpRequest, *args, **kwargs):
  if request.method == "POST":
    Post.objects.create(
      title =request.POST["title"],
      releaseYear =request.POST["releaseYear"],
      genre =request.POST["genre"],
      rating =request.POST["rating"],
      runningTime =request.POST["runningTime"],
      review =request.POST["review"],
      director =request.POST["director"],
      actor =request.POST["actor"],
    )
    return redirect("/")
  return render(request, "posts/posts_create.html")
