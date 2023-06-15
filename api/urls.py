from django.urls import path
from .views import MusicListAPIView, MusicDetailAPIView

urlpatterns = [
    # URL pattern for the music list view.
    path("music-list/", MusicListAPIView.as_view(), name="music-list"),
    
    # URL pattern for the music detail view.
    path("music-list/<str:pk>/", MusicDetailAPIView.as_view(), name="music-detail")
]