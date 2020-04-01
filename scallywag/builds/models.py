from django.db import models
from django_unixdatetimefield import UnixDateTimeField

class Jobs(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)
    srcpkg = models.TextField(blank=True, null=False)
    hash = models.TextField('commit', null=False)
    user = models.TextField(null=False)
    status = models.TextField(blank=True, null=True)
    logurl = models.TextField(blank=True, null=True)
    start_timestamp = UnixDateTimeField(blank=True, null=True)
    end_timestamp = UnixDateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jobs'
