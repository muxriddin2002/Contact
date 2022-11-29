from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=32)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
