from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from app.views import TodoList, TodoDetail, TodoCreate, TodoUpdate, TodoDelete, listar
from django.contrib import admin

urlpatterns = patterns('',
   # url(r"^$", TemplateView.as_view(template_name="base.html"), name="home"),
    # Examples:
    # url(r'^$', 'project_name.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    # url(r'^login/$', LoginView.as_view(template_name='userprofile/login.html'), name="login"),
    url(r"^account/", include("account.urls")),
    url(r'^$', TodoList.as_view(), name="app_list"),
    url(r'^Todo(?P<pk>\d+)$', TodoDetail.as_view(), name="app_detail"),
    url(r'^New$', TodoCreate.as_view(), name="app_create"),
    url(r'^Todo(?P<pk>\d+)/Update$', TodoUpdate.as_view(), name="app_update"),
    url(r'^Todo(?P<pk>\d+)/Delete$', TodoDelete.as_view(), name="app_delete"),
    url(r'^listar/todos$', 'app.views.listar'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
