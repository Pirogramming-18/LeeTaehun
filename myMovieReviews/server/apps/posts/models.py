from django.db import models

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=64)
  releaseYear = models.IntegerField()
  genre = models.CharField(max_length=32)
  rating = models.FloatField()
  runningTime = models.IntegerField()
  review =  models.TextField()
  director = models.CharField(max_length=32)
  actor = models.CharField(max_length=256)
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)