from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Banners(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image = ProcessedImageField(upload_to='banners',
                                processors=[ResizeToFill(1140,350)],
                                format='JPEG',
                                options={'quality': 90}, null=True, blank=True)
    class Meta:
        verbose_name_plural = 'banners'
    def __unicode__(self):
        return self.name

def get_banner_images():
    images = Banners.objects.all().order_by('-name')
    return images

class Faq(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    def __unicode__(self):
        return self.question

def get_faqs():
    questions = Faq.objects.all()
    return questions

class HomepageInfo(models.Model):
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=100)
    facebook = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    address3 = models.CharField(max_length=100)
    motto = models.TextField(max_length = 500)
    main_flyout = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Homepage Information'
