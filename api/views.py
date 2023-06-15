from rest_framework import generics, permissions
from .models import Music
from .serializers import MusicSerializer
from rest_framework.response import Response

# Music Views


class MusicListAPIView(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Set the owner of the music to the authenticated user
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        # Get the authenticated user
        user = self.request.user
        # Retrieve music based on access rights
        private_music = Music.objects.filter(owner=user)
        public_music = Music.objects.filter(access_type="public")
        print(public_music)
        protected_music = Music.objects.filter(access_type="protected", shared_with=user)
        # print(protected_music)
        # Create a list to store the serialized music data
        data_list = []

        # Serialize each category of music and add it to the data list
        for music_types in [public_music, private_music, protected_music]:
            serializer = MusicSerializer(music_types, many=True)
            data_list.append(serializer.data)
        
        
        return Response(data_list)

class MusicDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticated]

    # This view allows retrieving a specific music object, updating its details, or deleting it.
    # - The retrieve() method retrieves a specific music object.
    # - The update() method updates the details of a specific music object.
    # - The destroy() method deletes a specific music object.
