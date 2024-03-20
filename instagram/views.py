from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from .models import *
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class ExampleApiView(APIView):
    # permission_classes = [IsAuthenticated]
    pass


class ReelsApiView(ExampleApiView):

    def get(self, request):
        videos_obj = Video.objects.all()
        videos = ReelsSerializer(instance=videos_obj, many=True)
        return Response({'videos': videos.data})

    def post(self, request):
        user = User.objects.get(id=request.POST.get('user'))
        video = Video.objects.get(id=request.POST.get('video'))

        if Like.objects.filter(user=user, video=video).exists():
            Like.objects.get(user=user, video=video).delete()
            return Response("Successfully deleted like", status=status.HTTP_204_NO_CONTENT)
        else:
            Like.objects.create(user=user, video=video)
            return Response("Successfully added like", status=status.HTTP_200_OK)



class RecommendationApiView(ExampleApiView):

    def get(self, request):
        videos_obj = Video.objects.all().order_by('-likes')

        videos = RecommendationSerializer(instance=videos_obj, many=True)
        return Response({'videos': videos.data})