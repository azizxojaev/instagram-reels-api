from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver
from .models import Like


@receiver(pre_delete, sender=Like)
def decrease_like_count(sender, instance, **kwargs):
    liked_video = instance.liked_video
    liked_video.likes -= 1
    liked_video.save()

@receiver(pre_save, sender=Like)
def increase_like_count(sender, instance, **kwargs):
    liked_video = instance.liked_video
    liked_video.likes += 1
    liked_video.save()