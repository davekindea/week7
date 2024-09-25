from rest_framework import serializers

class SalesDataSerializer(serializers.Serializer):
    sales = serializers.ListField(child=serializers.FloatField())