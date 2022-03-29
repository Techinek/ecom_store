from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)
        return (TaggedItem.objects.select_related('tag').
                filter(content_type=content_type, object_id=obj_id))


class Tag(models.Model):
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label


class TaggedItem(models.Model):
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE,
                            related_name='tagged_items')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     related_name='tagged_items')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
