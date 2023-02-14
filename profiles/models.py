from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250, blank=True)
    content = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to='images/',
        default='../l8qeltsgnl3r9lyfrg5v'
    )
    balance = models.IntegerField(null=True)
    gym_category = models.IntegerField(default=1)
    tutorial_level = models.IntegerField(default=1)
    trainer_type = models.TextField(default='Trainer')
    elite_level = models.IntegerField(default=1)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.trainer_type} {self.owner}"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
