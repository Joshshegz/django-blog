from django.db import models
from django.conf import settings
from django.utils import timezone
from django.shortcuts import reverse


#USing a model manager to filter published blogs
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(choices=Blog.Status.PUBLISHED)
    

# Create your models here.
class Blog(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        ARCHIVED = 'AR', 'Archived'
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blogs')
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    choices = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    tags = models.ManyToManyField('Tags', blank=True)
    publish =models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated =models.DateTimeField(auto_now=True) 


    objects = models.Manager()
    published = PublishedManager()
    
class Meta:
    ordering = ['-publish']
    indexes = [ models.Index(fields=['-publish']), ]
    
    def __str__(self): 
        return self.title


def get_absolute_url(self):
    return reverse( 'blog:post_detail', args=[self.id] )

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=500, blank=True)

#     def __str__(self):
#         return self.user.username

class Tags(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)


    def __str__(self):
        return self.name 
    
