from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django import *
from django.contrib.gis.feeds import Feed
# Create your models here.
from django.db.models import permalink
import datetime
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.title


class RSSFeed(Feed):
    title = "My awesome blog feed"
    description = "The latest from my awesome blog"
    link = "/blog/"
    item_link = link

    def items(self):
        return BlogPost.objects.all()[:10]
    
def content_file_name(instance, filename):
    return '/'.join(['images', instance.art.name, filename])

class Category(models.Model):
    """A content category"""
    label = models.CharField(blank=True, max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.label

class Art(models.Model):
    name = models.CharField('artity',max_length = 20)
    description = models.TextField('synopsis', max_length= 200)
    image = models.ImageField(upload_to = content_file_name,default = 'shop image')
    caption = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField()
    blogpost = models.ForeignKey(BlogPost)
    #category = models.ForeignKey(Category, default = None)

 
    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('art_detail', None, {'slug': self.slug})
    
    def save(self):
        self.modified = datetime.datetime.now()
        super(Art, self).save()

    objects = models.Manager()
    
