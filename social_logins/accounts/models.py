from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    """
    Model definition for User.
    This model will contain details of users.
    """
    social_id = models.CharField(max_length=255, null=True, blank=True, default=True)

    def __str__(self):
        return self.email
