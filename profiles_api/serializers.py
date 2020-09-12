from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length = 10)
    # will accept any character input that is less than 10 chars
