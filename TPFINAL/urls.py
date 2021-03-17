from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.views.static import serve


urlpatterns = [
	url(r'^admin/', admin.site.urls),
    url(r'', include ('apps.noticias.urls')),
    url(r'^usuario/', include ('apps.usuario.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]

urlpatterns +=[
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
        })
]