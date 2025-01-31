from rest_framework import serializers


class InfoSerializer(serializers.Serializer):
    email = serializers.EmailField()
    current_datetime = serializers.DateTimeField()
    github_url = serializers.URLField()
