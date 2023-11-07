# members/views.py
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Member, Event, Content, CampusDon  # Import the CampusDon model
from .serializers import MemberSerializer, EventSerializer, ContentSerializer, CampusDonSerializer  # Import the serializer

# Existing viewsets for Member, Event, and Content
class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

# New viewset for CampusDon
class CampusDonViewSet(viewsets.ModelViewSet):
    queryset = CampusDon.objects.all()
    serializer_class = CampusDonSerializer

def landing_page(request):
    return HttpResponse("<h1>Welcome to ClubApp!</h1>")

