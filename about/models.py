from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Pastor(models.Model):
    class Meta:
        verbose_name_plural = 'pastor'
    photo = ProcessedImageField(upload_to='about/pastor',
                                processors=[ResizeToFill(200,200)],
                                format='JPEG',
                                options={'quality': 90}, null=True, blank=True)
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True, blank=True)

class Beliefs(models.Model):
    class Meta:
        verbose_name_plural = 'beliefs'
    text = models.TextField(null=True, blank=True)

class WorshipTeam(models.Model):
    class Meta:
        verbose_name_plural = 'Worship Team'
    bio = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)

class Video(models.Model):
    class Meta:
        verbose_name_plural = 'Youtube Links'
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    visible = models.BooleanField(default=False)
    front_page = models.BooleanField(default=False)
    video_link = models.CharField(max_length=500)

class Music(models.Model):
    class Meta:
        verbose_name_plural = 'Music Files'
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    date_recorded = models.DateTimeField()
    music = models.FileField(upload_to='about/worship_team')

class SermonSeries(models.Model):
    class Meta:
        verbose_name_plural= 'Sermon Series'
    title = models.CharField(max_length=100, null=True, blank=True)
    image = ProcessedImageField(upload_to='about/sermon_series',
                                processors=[ResizeToFill(1200,720)],
                                format='JPEG',
                                options={'quality': 90}, null=True, blank=True)
    body = models.TextField(null=True, blank=True)

def get_videos():
    videos = Video.objects.filter(visible=True)
    return videos

def get_homepage_videos():
    videos = Video.objects.filter(visible=True, front_page=True)
    return videos
