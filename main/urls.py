from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Fitocode Backend APIs",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('main.apps.user.urls')),
    path('', include('main.apps.management.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('estimate/', include('main.apps.estimate.urls')),

    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
