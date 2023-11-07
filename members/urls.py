# members/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, EventViewSet, ContentViewSet, CampusDonViewSet  # Import the CampusDonViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'events', EventViewSet)
router.register(r'contents', ContentViewSet)
router.register(r'campus-dons', CampusDonViewSet)  # Register the CampusDonViewSet with the router

urlpatterns = [
    path('', include(router.urls)),  # Include the router urls in the urlpatterns
]

