from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^catalog/', include('catalog.urls')),
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
#
# urlpatterns += [                                        We can add urlpattern's ( += )
#     url(r'^catalog/', include('catalog.urls')),
#     url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
# ]
#
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

