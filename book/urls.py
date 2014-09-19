from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'book.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'learn_words.views.home', name='home'),
    url(r'^register/$', 'learn_words.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^profile/$', 'learn_words.views.profile', name='profile'),
    url(r'^article/(?P<word_id>\d+)/$', 'learn_words.views.article', name='article'),
    url(r'^newword/$', 'learn_words.views.newword', name='newword'),
    url(r'^admin/', include(admin.site.urls)),
)
