from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db.models.signals import post_save

class UserProfile(models.Model):

    # This field is required by Django
    user = models.OneToOneField(User, related_name="profile")
    # These are our custom extensions
    photo = ProcessedImageField(upload_to='accounts/photos',
                                processors=[ResizeToFill(200,200)],
                                format='JPEG',
                                options={'quality': 90}, null=True, blank=True)
    equipment = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    role = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return User.objects.get(id=self.user_id).username

# Automatically creates a profile for every user
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
