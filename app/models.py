from django.db import models

class Video(models.Model):
    file = models.FileField(upload_to='videos/')

class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='subtitles')
    timestamp = models.FloatField()
    text = models.TextField()
