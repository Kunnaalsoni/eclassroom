from rest_framework import serializers
from .models import ClassContent


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassContent
        fields = '__all__'