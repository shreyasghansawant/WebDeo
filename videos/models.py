from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator


class Video (models.Model):
    thumbnail = models.ImageField (upload_to='thumbnails/', default=None)
    title = models.CharField (max_length=40)
    video = models.FileField (upload_to='videos/', validators=[FileExtensionValidator (allowed_extensions=['mp4'])])
    description = models.TextField ()
    date = models.DateField (auto_now_add=True)
    time = models.TimeField (auto_now_add=True)
    views = models.IntegerField (default=0)
    admin = models.ForeignKey (User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Profile (models.Model):
    profile_picture = models.ImageField (upload_to='profiles/', default="/profiles/NO_DP.jpg")
    date_of_birth = models.DateField (default=timezone.now)
    user = models.OneToOneField (User, on_delete=models.CASCADE)
    bio = models.CharField (max_length=100, default="No Bio")

    def __str__(self):
        return self.user.username


class Like (models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    video = models.ForeignKey (Video, on_delete=models.CASCADE)
    date_time = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return self.video.title + ' - ' + self.user.username


class Comment (models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    video = models.ForeignKey (Video, on_delete=models.CASCADE)
    date_time = models.DateTimeField (auto_now_add=True)
    text = models.TextField ()

    def __str__(self):
        return self.video.title + ' - ' + self.user.username
