# members/views.py

from django.http import HttpResponse
from rest_framework import viewsets
from .models import Member, Event, Content
from .serializers import MemberSerializer, EventSerializer, ContentSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


def landing_page(request):
    return HttpResponse("<h1>Welcome to ClubApp!</h1>")
