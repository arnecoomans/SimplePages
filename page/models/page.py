from django.db import models
from django.contrib.sites.models import Site
# https://docs.djangoproject.com/en/4.2/ref/contrib/sites/
from django.contrib.auth.models import User
from django.utils.timezone import now

class Page(models.Model):
  site              = models.ForeignKey(Site, on_delete=models.CASCADE)
  title             = models.CharField(max_length=255)

  meta_description  = models.CharField(max_length=255, blank=True)
  
  is_default        = models.BooleanField(default=False)
  is_in_menu        = models.BooleanField(default=True)

  #content             = models.TextField(blank=True, help_text='Markdown Supported')
  # Meta
  date_created      = models.DateTimeField(auto_now_add=True)
  date_modified     = models.DateTimeField(auto_now=True)
  date_published    = models.DateTimeField(default=now)
  user              = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.title
  
  class Meta:
    ordering = (['site', 'date_created'])
    db_table = 'pages'
    # constraints = [
    #     models.UniqueConstraint(fields=['site', 'is_default'], name='unique appversion')
    # ]