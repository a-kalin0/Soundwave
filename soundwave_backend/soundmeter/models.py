from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sound(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    duration = models.IntegerField(null=True)
    min_db_size = models.IntegerField(null=True)
    max_db_size = models.IntegerField(null=True)
    avg_db_size = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, verbose_name='propriétaire', on_delete=models.CASCADE)
    is_shared = models.BooleanField(default=False)
    location = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'sound'
        verbose_name_plural = 'sounds'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/{self.slug}/'