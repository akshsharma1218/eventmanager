from django.db import models
from django.utils import timezone
from django.urls import reverse

class Event(models.Model):
    event_name  = models.CharField(max_length=100)
    data        = models.TextField(null=True)
    time        = models.DateTimeField(default=timezone.now)
    location    = models.CharField(max_length=100)
    is_liked    = models.BooleanField(default=False)
    image       =models.ImageField(default='default_vumatg.png', upload_to='event_pics')

    def __str__(self):
        return self.event_name

    def get_absolute_url(self):
        return reverse('home')
