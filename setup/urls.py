from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()

# URLs do site
urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('apps.blog.urls')),

    # URLs da API
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include(router.urls)),
    path('api/blog/', include('apps.blog.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += router.urls

