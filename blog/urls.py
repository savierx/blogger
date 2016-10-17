from django.conf.urls import url
from django.contrib.gis.feeds import Feed
#from blog.views import archive
from blog.models import RSSFeed, Art, BlogPost, Category
from .views import *
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    #url(r'^(?P<slug>[-\w]+)/detail/$', views.detail, name = 'detail'),
    #url(r'^(?P<slug>[-\w]+)/result/$', views.results, name = 'result'),
    #url(r'^(?P<pk>[0-9]+)/vote/$',views.vote , name="vote"),
    ############################################################
    url(r'^$', ArchiveView),
    url(r'^(?P<url>.*)/feeds/$', Feed, {'feed_dict': {'rss': RSSFeed}}),
    url(r'^(?P<pk>[0-9]+)/$', ArtView.as_view , name="blogart"),
    url(r'^(?P<pk>[0-9]+)/blogpost/$', HomeView.as_view , name="bloghome"),
    url(r'^(?P<pk>[-\w]+category/)/$', CategoryView.as_view , name="blogcategory"),
    url(r'^search/$', search , name="blogsearch"),
]
