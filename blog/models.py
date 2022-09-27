from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

# Create your models here.
class Post(models.Model):
  title = models.CharField('Title', max_length=100, null=True, blank=True)
  summary = models.TextField('Summary', blank=True)
  content = models.TextField('Content', blank=True)
  slug = models.SlugField(unique=True)
  created_at = models.DateTimeField('Created At', auto_now_add=True)
  modified_at = models.DateTimeField('Modified At', auto_now=True)
  published_at = models.DateTimeField('Published At', null=True, blank=True)
  hero_image = VersatileImageField(
    upload_to="hero_images", ppoi_field="ppoi", null=True, blank=True
  )
  ppoi = PPOIField(null=True, blank=True)

class Tag(models.Model):
  value = models.CharField(max_length=100, null=True, blank=True)

  class Meta:
    ordering = ["value"]
