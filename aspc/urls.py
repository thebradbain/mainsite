from django.conf.urls.defaults import patterns, include, url
from aspc.folio.models import Page

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    (r'(?P<slug_path>(?:[\w\-\d]+/)+)$', 'aspc.folio.views.page_view',),
    
    # Examples:
    # url(r'^$', 'aspc.views.home', name='home'),
    # url(r'^aspc/', include('aspc.foo.urls')),
)
