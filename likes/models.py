from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = get_user_model()


class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='liked_items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     related_name='liked_items')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
