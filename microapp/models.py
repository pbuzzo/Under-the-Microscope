from django.db import models
from django.contrib.auth.models import AbstractUser


class UsrModel(AbstractUser):
    bio = models.TextField(max_length=150, blank=True, null=True)
    url = models.URLField(max_length=30, blank=True)
    age = models.IntegerField(null=True, blank=True)

    def _str_(self):
        return self.username
