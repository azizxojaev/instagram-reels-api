from .views import *
from django.urls import path


urlpatterns = [
    path('reels/', ReelsApiView.as_view()),
    path('recommendations/', RecommendationApiView.as_view()),
]