from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    voice_data = models.FileField(upload_to='voice_samples/', null=True, blank=True)
    
    def __str__(self):
        return self.full_name