from django.conf.urls import url
from django.contrib.gis.feeds import Feed
#from blog.views import archive
from blog.models import RSSFeed, Art, BlogPost, Category
from .views import *

app_name = 'blog'
urlpatterns = [
    url(r'^$', ArchiveView),
    url(r'^feeds/(?P<url>.*)/$', Feed, {'feed_dict': {'rss': RSSFeed}}),
    url(r'^(?P<slug>[-\w]+)/$', ArtView.as_view , name="blogart"),
    url(r'^blogpost/(?P<pk>[0-9]+)/$', HomeView.as_view , name="bloghome"),
    url(r'^category/(?P<slug>[-\w]+)/$', CategoryView.as_view , name="blogcategory"),
    url(r'^search/$', search , name="blogsearch"),
]
