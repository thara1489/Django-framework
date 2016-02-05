from django.conf.urls import include, url
from django.contrib import admin
from register.views import Home
#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myuniversity.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
urlpatterns = [

  url(r'^$', 'Home. as_view()', name='home'),

  url(r'^admin/', include(admin.site.urls)),
]

#
 #   url(r'^register/', include('register.urls')),
#    url(r'^admin/', admin.site.urls),

