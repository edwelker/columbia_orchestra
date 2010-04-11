from django.db import models
from django.contrib import admin
from ThumbnailImageField import ThumbnailImageField

# Create your models here.

class OrchestraMember(models.Model):

    INSTRUMENTS = (
        (1, "Violin"),
        (2, "Viola"),
        (3, "Cello"),
        (4, "Bass"),
        (5, "Flute/Piccolo"),
        (6, "Oboe"),
        (7, "English Horn"),
        (8, "Clarinet"),
        (9, "Bass Clarinet"),    
        (10, "Bassoon"),
        (11, "Contra Bassoon"),
        (12, "Trumpet"),    
        (13, "Horn"),
        (14, "Trombone"),
        (15, "Bass Trombone"),
        (16, "Tuba"),
        (17, "Harp"),
        (18, "Piano"),
        (19, "Timpani"),
        (20, "Percussion"),
        (21, "Music Director"),
    )        

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)

    instrument = models.IntegerField(max_length=10, choices=INSTRUMENTS)

    bio = models.TextField()

    photo = ThumbnailImageField(upload_to='images/user_photos')

    class Meta: 
        ordering = ["instrument"]

    def __unicode__(self):
        return "%s %s %s, %s" % (self.first_name, self.middle_name, self.last_name, self.instrument)

    def get_absolute_url(self):
        return ('item_detail', None, { 'object_id': self.id })

admin.site.register(OrchestraMember)
