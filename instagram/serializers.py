from rest_framework.serializers import ModelSerializer
from .models import *


class ReelsSerializer(ModelSerializer):

    class Meta:
        model = Video
        exclude = ['id']
    
    def to_representation(self, instance):
        redata = super().to_representation(instance)
        redata['video'] = f"http://127.0.0.1:8000{redata['video']}"
        return redata


class RecommendationSerializer(ModelSerializer):

    class Meta:
        model = Video
        exclude = ['id']