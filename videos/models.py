from django.db import models


# Create your models here.
class Video(models.Model):
    video_title = models.CharField(max_length=100, null=True)
    video_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.video_title
