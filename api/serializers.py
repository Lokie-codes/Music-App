from rest_framework.serializers import ModelSerializer
from .models import Music
from rest_framework import serializers

class MusicSerializer(ModelSerializer):
   # The MusicSerializer is responsible for serializing and deserializing Music objects.

    # The owner field is a read-only field that represents the owner of the music.
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Music
        # The fields attribute specifies the fields to be included in the serialized representation of a Music object.
        fields = [ "title", "owner", "audio_file", "access_type", "created_at", "shared_with"]

    # No additional methods are overridden, as the ModelSerializer provides the necessary functionality for serialization and deserialization.
