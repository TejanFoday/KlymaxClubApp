# members/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, EventViewSet, ContentViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'events', EventViewSet)
router.register(r'contents', ContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
