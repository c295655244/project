from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import hello, current_datetime, hours_ahead,display_meta
#from mysite.books import views
from mysite.contact import views
#from mysite.views import hello, my_homepage_view


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^display/', display_meta),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search-form/$', 'mysite.views.search_form'),
    url(r'^search/$', 'mysite.views.search'),
    url(r'^contact/$', views.contact),
    url(r'^contact/thanks/$', views.contact_thanks),
    #url(r'^$', my_homepage_view),

)
