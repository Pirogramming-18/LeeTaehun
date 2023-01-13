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

def posts_update(request: HttpRequest, pk, *args, **kwargs):
  post = Post.objects.get(id=pk)
  
  if request.method == "POST":
      post.title =request.POST["title"]
      post.releaseYear =request.POST["releaseYear"]
      post.genre =request.POST["genre"]
      post.rating =request.POST["rating"]
      post.runningTime =request.POST["runningTime"]
      post.review =request.POST["review"]
      post.director =request.POST["director"]
      post.actor =request.POST["actor"]
      return redirect(f"/posts/{post.id}")
    
  return render(request, "posts/posts_update.html", {"post": post})

def posts_delete(request:HttpRequest, pk, *args, **kwargs):
  if request.method == "POST":
    post = Post.objects.get(id=pk)
    post.delete()
  return redirect("/")