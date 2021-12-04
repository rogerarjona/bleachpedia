"""
Base URL Configuration
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.views.decorators.cache import never_cache

# Admin Attributes
if hasattr(settings, 'ADMIN_SITE_HEADER'):
    admin.site.site_header = settings.ADMIN_SITE_HEADER
if hasattr(settings, 'ADMIN_SITE_TITLE'):
    admin.site.site_title = settings.ADMIN_SITE_TITLE
if hasattr(settings, 'ADMIN_SITE_INDEX_TITLE'):
    admin.site.index_title = settings.ADMIN_SITE_INDEX_TITLE
if hasattr(settings, 'SITE_URL'):
    admin.site.site_url = settings.SITE_URL


urlpatterns = [

    # Admin
    path('bleachpedia/', admin.site.urls),
    path('api/', include('bleachpedia.apps.api.urls')),
    path('crud/', include('bleachpedia.apps.crud.urls')),

    # DRF
    path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:

    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
