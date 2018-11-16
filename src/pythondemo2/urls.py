from django.conf.urls import url ,include

from django.contrib import admin
admin.autodiscover()

from blog.views import archive

urlpatterns =[
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^blog/', archive),
   # url(r'^admin/', admin.site.urls),
    #url(r'^blog/', include(('blog.urls', "blog"), namespace="blog")),
]
