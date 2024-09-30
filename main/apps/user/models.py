import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from main.apps.user.manager import UserManager


class User(AbstractUser):
    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_("email address"), unique=True)
    birthday = models.DateField(null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self) -> str:
        return str(self.email)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
