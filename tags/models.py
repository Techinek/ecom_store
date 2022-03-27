from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            related_name='tagged_items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     related_name='tagged_items')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
