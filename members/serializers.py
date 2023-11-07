from rest_framework import serializers
from .models import Member, Event, Content, CampusDon

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

# New serializer for the CampusDon model
class CampusDonSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampusDon
        fields = '__all__'  # to serialize all fields from CampusDon
