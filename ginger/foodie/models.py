from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    type = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    photo_url = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    vendors = models.ManyToManyField(Vendor, null=True, blank=True)
    fb_id = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name
