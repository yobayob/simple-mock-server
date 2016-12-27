from django.contrib.sitemaps import Sitemap
from models import *


class StaticViewSitemap(Sitemap):
    priority = 1
    changefreq = 'monthly'

    def items(self):
        return ['start_page', 'home', 'map', 'form']

    def location(self, item):
        return reverse(item)


class OrgsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def location(self, obj):
        return obj.get_absolute_url()

    def items(self):
        return Orgs.objects.all()

    def lastmod(self, obj):
        return obj.changed


class SocialServiceSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def location(self, obj):
        return obj.get_absolute_url()

    def items(self):
        return SocialService.objects.all()

    def lastmod(self, obj):
        return obj.changed

map = { 'static': StaticViewSitemap,
        #'orgs': OrgsSitemap,
        #'social_service':SocialServiceSitemap,
        }