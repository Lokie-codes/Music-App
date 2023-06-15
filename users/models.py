from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from users.user_manager import UserManager

# User Model
class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)  # Email field for the user (unique)
    REQUIRED_FIELDS = []  # Fields required when creating a user
    USERNAME_FIELD = 'email'  # Field used for authentication (username field is set to email)
    objects = UserManager()  # Manager class for the user model

    def __str__(self):
        return self.email