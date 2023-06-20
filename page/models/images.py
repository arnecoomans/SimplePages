from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
  source            = models.ImageField()
  description       = models.CharField(max_length=255)
  # Meta
  date_created      = models.DateTimeField(auto_now_add=True)
  date_modified     = models.DateTimeField(auto_now=True)
  user              = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return f"{ self.description } ({ self.source })"