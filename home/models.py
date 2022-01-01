from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Device(models.Model):
    name = models.CharField(max_length=50)


class Location(models.Model):
    name = models.CharField(max_length=50)


class FloorPlan(models.Model):
    name = models.CharField(max_length=50)


class DeviceLocation(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=36, db_index=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    location = models.ForeignKey(Location, models.PROTECT, blank=True, null=True)
    floorplan = models.ForeignKey(FloorPlan, models.PROTECT, blank=True, null=True)
