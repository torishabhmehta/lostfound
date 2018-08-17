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

class TitleSerializer(serializers.Serializer):
    item_id = serializers.AutoField(primary_key=True)
    item_name = serializers.CharField(max_length=255)
