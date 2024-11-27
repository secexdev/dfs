from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dns_filter_app.urls')),
]



from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="DNS Filter API",
      default_version='v1',
      description="API for DNS filtering and parental control",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@dnsfilter.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.IsAuthenticated],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dns_filter_app.urls')),
    path('swagger/', schema_view.as_view()),
]
