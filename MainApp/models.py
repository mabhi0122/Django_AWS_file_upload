from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extensions, validate_file_size

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    profile = models.ImageField(upload_to='profile_pics/', validators=[validate_file_size, validate_file_extensions])
    resume = models.FileField(upload_to='resumes/', )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.profile}"
    