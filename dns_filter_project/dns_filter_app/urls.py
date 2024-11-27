from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from .views import BlocklistViewSet, DNSLogViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Setup router for viewsets
router = DefaultRouter()
router.register(r'blocklists', BlocklistViewSet)
router.register(r'dnslogs', DNSLogViewSet)

# Setup schema view for Swagger
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

# Define URL patterns
urlpatterns = [
    path('api/', include(router.urls)),
        path('', include('dns_filter_app.urls')),  
    path('swagger/', schema_view.as_view()),
]
