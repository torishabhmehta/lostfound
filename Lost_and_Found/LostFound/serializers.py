from .models import *
from rest_framework import serializers

# Create Lost Serialiser

class LostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = '__all__'

# Create Found Serialiser

class FoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Found
        fields = '__all__'

# Create Spam Serialiser

class SpamSerializer(serializers.Serializer):
    instance_id = serializers.IntegerField(max_value=None, min_value=None)
    item_name = serializers.CharField(max_length=255)
    item_desc = serializers.CharField(max_length=255)
