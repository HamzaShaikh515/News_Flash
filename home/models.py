from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Country(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Status(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Language(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

obj = Status.objects.get(name='Draft')
class Article(models.Model):
    author = models.ForeignKey(User,default='' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='articles/', default='')
    summary = models.CharField(max_length=255,default='')
    content = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default='')
    language = models.ForeignKey(Language, on_delete=models.CASCADE,default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE,default='')
    published_date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    unique_id = models.CharField(max_length=20, default='') 
    status = models.ForeignKey(Status, on_delete=models.CASCADE,default=obj.pk)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.unique_id = uuid.uuid4().hex[:20]
        super(Article,self).save(*args,**kwargs)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    commenter_name = models.ForeignKey(User,default='' ,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.commenter_name} on {self.article.title}'

