# This tells Django how to turn our `Movie` model into JSON.

from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    # Meta class provides additional settings for ModelSerializer.
    class Meta:
        model = Movie  # Points to the Movie model for serialization
        fields = '__all__'  # Includes all fields of the Movie model in the serializer ['title', 'release_date']