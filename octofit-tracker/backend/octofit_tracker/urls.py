# Placeholder for URLs
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import api_root

router = DefaultRouter()

urlpatterns = [
    path('', api_root, name='api-root'),  # Root endpoint
    path('api/', include(router.urls)),
]
