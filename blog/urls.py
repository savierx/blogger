from django.conf.urls import url
from django.contrib.gis.feeds import Feed
from blog.views import archive
from blog.models import RSSFeed

urlpatterns = [
    url(r'^$', archive),
    url(r'^feeds/(?P<url>.*)/$', Feed, {'feed_dict': {'rss': RSSFeed}}),
]
