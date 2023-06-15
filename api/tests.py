from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from users.models import CustomUser
from .models import Music
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Music model tests


class MusicModelTestCase(TestCase):
    # Set up necessary objects for testing the Music model
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create(username="testuser")

        # Create a test audio file
        audio_file = SimpleUploadedFile(
            "test_audio.mp3", b"file_content", content_type="audio/mpeg"
        )

        # Create a test music object
        self.music = Music.objects.create(
            title="Test Music",
            owner=self.user,
            audio_file=audio_file,
            access_type="public",
        )

    def test_music_model(self):
        """
        Test Music model fields and properties.
        """
        music = self.music
        self.assertEqual(music.title, "Test Music")
        self.assertEqual(music.owner, self.user)
        self.assertEqual(music.access_type, "public")
        self.assertIsNotNone(music.created_at)

    def test_music_model_str_representation(self):
        """
        Test the string representation of the Music model.
        """
        music = self.music
        expected_str = f"{music.title} - {music.owner}"
        self.assertEqual(str(music), expected_str)

    def test_music_model_shared_with(self):
        """
        Test adding and removing users from the shared_with field.
        """
        music = self.music
        self.assertFalse(music.shared_with.exists())

        # Add a user to the shared_with field
        shared_user = CustomUser.objects.create(email="test@musicapp.com")
        music.shared_with.add(shared_user)
        self.assertTrue(music.shared_with.exists())
        self.assertIn(shared_user, music.shared_with.all())

        # Remove the user from the shared_with field
        music.shared_with.remove(shared_user)
        self.assertFalse(music.shared_with.exists())

    def tearDown(self):
        """
        Clean up after the test by deleting the test music object and associated files.
        """
        self.music.audio_file.delete()
        self.music.delete()
        self.user.delete()


# Music views API tests


class MusicListAPIViewTestCase(APITestCase):
    # Set up necessary objects for testing the MusicListAPIView
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)

    def test_get_music_list(self):
        """
        Test the retrieval of the music list.
        """
        # Create some test music objects
        music1 = Music.objects.create(
            title="Music 1", owner=self.user, access_type="public"
        )
        music2 = Music.objects.create(
            title="Music 2", owner=self.user, access_type="private"
        )
        music3 = Music.objects.create(
            title="Music 3", owner=self.user, access_type="protected"
        )
        music3.shared_with.add(self.user)

        url = reverse("music-list")
        response = self.client.get(url)
        music_list = response.data
        music_titles = []
        for orderedDict in music_list:
            for music in orderedDict:
                music_titles.append(music['title'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(music_list), 3)
        self.assertIn("Music 1", music_titles)
        self.assertIn("Music 2", music_titles)
        self.assertIn("Music 3", music_titles)

    def test_create_music(self):
        """
        Test the creation of a new music object.
        """
        url = reverse("music-list")
        audio_file = SimpleUploadedFile(
            "test_audio.mp3", b"file_content", content_type="audio/mpeg"
        )
        data = {
            "title": "New Music",
            "audio_file": audio_file,
            "access_type": "public",
            "shared_with": []
        }
        response = self.client.post(url, data)
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Music.objects.count(), 1)
        self.assertEqual(Music.objects.first().title, "New Music")

    def tearDown(self):
        """
        Clean up after the test by logging out and deleting the test user.
        """
        self.client.logout()
        self.user.delete()


class MusicDetailAPIViewTestCase(APITestCase):
    # Set up necessary objects for testing the MusicDetailAPIView
    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)

        # Create a test music object
        self.music = Music.objects.create(
            title="Test Music",
            owner=self.user,
            access_type="public",
        )

    def test_get_music_detail(self):
        """
        Test the retrieval of a music object detail.
        """
        url = reverse("music-detail", kwargs={"pk": self.music.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Music")

    def test_update_music(self):
        """
        Test updating a music object.
        """
        url = reverse("music-detail", kwargs={"pk": self.music.pk})
        data = {"title": "Updated Music"}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Music.objects.first().title, "Updated Music")

    def test_delete_music(self):
        """
        Test deleting a music object.
        """
        url = reverse("music-detail", kwargs={"pk": self.music.pk})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Music.objects.count(), 0)

    def tearDown(self):
        """
        Clean up after the test by logging out and deleting the test user.
        """
        self.client.logout()
        self.user.delete()
