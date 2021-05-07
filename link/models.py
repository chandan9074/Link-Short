from django.db import models
from django.utils.crypto import get_random_string
from accounts.models import UserProfile
import uuid

# Create your models here.

class Url(models.Model):
    title = models.CharField(max_length=200, default=uuid.uuid1, unique=True)
    given_link = models.CharField(max_length=2000)
    short_link = models.CharField(max_length=500, blank=True, unique=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)

    def save(self, *args, **kwargs):
        string = self.short_link
        
        if not string:
            self.short_link = get_random_string(7).lower()
        super(Url, self).save(*args, **kwargs)


