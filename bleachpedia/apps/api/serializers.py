from rest_framework import serializers
from .models import Shinigami


class ShinigamiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shinigami
        fields = "__all__"
