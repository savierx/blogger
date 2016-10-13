from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django import *
from django.contrib.gis.feeds import Feed
#from django.contrib.syndication.feeds import Feed
# Create your models here.
from django.db.models import permalink
#from markdown import markdown
import datetime
from django.contrib import admin

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)


class RSSFeed(Feed):
    title = "My awesome blog feed"
    description = "The latest from my awesome blog"
    link = "/blog/"
    item_link = link

    def items(self):
        return BlogPost.objects.all()[:10]
    
def content_file_name(instance, filename):
    return '/'.join(['images', instance.art.name, filename])

class Art(models.Model):
    name = models.CharField('shop name',max_length = 20)
    description = models.TextField('item description', max_length= 200)
    image = models.ImageField(upload_to = content_file_name,default = 'shop image')
    caption = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField()
    blogpost = models.ForeignKey(BlogPost)

 
    def __str__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('art_detail', None, {'object_id': self.id})
    
#if field is slug ; return ("cms-story", (), {'slug': self.slug})
    def save(self):
        #self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Story, self).save()

    admin_objects = models.Manager()
    #objects = ViewableManager()
    
class Category(models.Model):
    """A content category"""
    label = models.CharField(blank=True, max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.label
    
#class ViewableManager(models.Manager):
 #   def get_query_set(self):
  #      default_queryset = super(ViewableManager, self).get_query_set()
   #     return default_queryset.filter(status__in=VIEWABLE_STATUS)


