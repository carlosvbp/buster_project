from movies.models import Movie, Note
from rest_framework import serializers
from users.serializers import UserSerializer


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_blank=True, default="")
    rating = serializers.ChoiceField(choices=Note.choices, default=Note.G)
    synopsis = serializers.CharField(allow_blank=True, default="")
    added_by = serializers.CharField(read_only=True, source="user.email")

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
