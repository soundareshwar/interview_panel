from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'panels_rout.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^interview/', include('panel_inter_app.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
