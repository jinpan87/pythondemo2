from django.conf.urls import url ,include
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

from blog.views import archive

urlpatterns =[
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/$', archive),

    url(r'^admin/', admin.site.urls),
    #url('', TemplateView.as_view(template_name='index.html'))
    #url(r'^blog/', TemplateView.as_view(template_name='archive.html')),
    #url(r'^admin/', admin.site.urls),
    #url(r'^blog/', include(('blog.urls', "blog"), namespace="blog")),
]
