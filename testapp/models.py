from django.db import models

class Location(models.Model):
    location_id = models.IntegerField(null=True,blank=True)
    client_id = models.IntegerField(null=True,blank=True)
    timestamp = models.DateTimeField()
    
    def __unicode__(self):
        return unicode(self.location_id)