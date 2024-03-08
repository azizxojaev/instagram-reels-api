from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated


class ExampleApiView(APIView):
    permission_classes = [IsAuthenticated]


class ReelsApiView(ExampleApiView):

    def get(self, request):
        videos_obj = Video.objects.all()
        videos = ReelsSerializer(instance=videos_obj, many=True)
        return Response({'videos': videos.data})


class RecommendationApiView(ExampleApiView):

    def get(self, request):
        videos_obj = Video.objects.all().order_by('-likes')

        videos = RecommendationSerializer(instance=videos_obj, many=True)
        return Response({'videos': videos.data})