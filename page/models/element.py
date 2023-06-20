from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

from .page import Page
from .images import Image


class Element(models.Model):
  page              = models.ManyToManyField(Page)

  anchor            = models.CharField(blank=True, max_length=64)
  title             = models.CharField(blank=True, max_length=255
                                       )
  content           = models.TextField(blank=True, help_text='HTML or Markdown Supported')
  
  hero_image        = models.ForeignKey(Image, blank=True, null=True, related_name='hero_image_for', on_delete=models.DO_NOTHING)
  background_image  = models.ForeignKey(Image, blank=True, null=True, related_name='background_image_for', on_delete=models.DO_NOTHING)

  order             = models.IntegerField(default=1)
  class FormatChoices(models.IntegerChoices):
    plain_text        = 0
    markdown          = 1
    html              = 2
    image             = 3
  format            = models.IntegerField(choices=FormatChoices.choices)

  HeroTemplateChoices = [('hero-none',  'No Hero'),
                        ('hero-left',   'Hero Left'),
                        ('hero-right',  'Hero Right'),
                        ('hero-solo',   'Hero Solo')]
  hero_template       = models.TextField(choices=HeroTemplateChoices, default="hero-left")

  ContentTemplateChoices = [('one-col',   'One Column Text'),
                            ('two-col',   'Two Column Text'),
                            ('three-col', 'Three Column Text')]
  content_template    = models.TextField(choices=ContentTemplateChoices, default="one_col")


  class StatusChoices(models.IntegerChoices):
    deleted           = 0
    revoked           = 1
    need_rework       = 2
    draft             = 3
    in_review         = 4
    published         = 5
  status            = models.IntegerField(choices=StatusChoices.choices)

  # Meta
  date_created      = models.DateTimeField(auto_now_add=True)
  date_modified     = models.DateTimeField(auto_now=True)
  date_published    = models.DateTimeField(default=now)
  user              = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self) -> str:
    return self.content[:64]
  
  class Meta:
    ordering = (['date_created'])
    #db_table = 'pages'
    # constraints = [
    #     models.UniqueConstraint(fields=['site', 'is_default'], name='unique appversion')
    # ]