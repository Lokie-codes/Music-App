from django.db import models
from users.models import CustomUser


# list of access types
ACCESS_TYPE = (
    ("public", "Public"),
    ("private", "Private"),
    ("protected", "Protected"),
)


# Music Model
class Music(models.Model):
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to="audiofiles/", help_text="Upload audio file")
    access_type = models.CharField(max_length=10, choices=ACCESS_TYPE, default="public")
    created_at = models.DateTimeField(auto_now_add=True)
    shared_with = models.ManyToManyField(CustomUser, related_name="sharedwith", blank=True, default=None)

    def __str__(self):
        return f"{self.title} - {self.owner}"

