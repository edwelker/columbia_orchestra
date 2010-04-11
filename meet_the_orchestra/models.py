from django.db import models
from django.contrib import admin
from ThumbnailImageField import ThumbnailImageField

# Create your models here.

class OrchestraMember(models.Model):

    INSTRUMENTS = (
        (1, "Violin I"),
        (2, "Violin II"),
        (3, "Viola"),
        (4, "Cello"),
        (5, "Bass"),
        (6, "Flute/Piccolo"),
        (7, "Oboe"),
        (8, "English Horn"),
        (9, "Clarinet"),
        (10, "Bass Clarinet"),    
        (11, "Bassoon"),
        (12, "Contra Bassoon"),
        (13, "Trumpet"),    
        (14, "French Horn"),
        (15, "Trombone"),
        (16, "Bass Trombone"),
        (17, "Tuba"),
        (18, "Harp"),
        (19, "Piano/Keyboard"),
        (10, "Timpani"),
        (21, "Percussion"),
        (22, "Alto Flute"),
        (23, "Eb Clarinet"),
        (24, "Tenor Saxophone"),
        (25, "Assistant Conductor"),
        (26, "Music Director"),
    )        

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)

    instrument = models.IntegerField(max_length=10, choices=INSTRUMENTS)
    principal = models.BooleanField()

    bio = models.TextField(help_text="Wrap paragraphs in '&lt;p&gt;...&lt;/p&gt;'")

    photo = ThumbnailImageField(upload_to='images/user_photos')
    
    former_member = models.BooleanField(help_text="Use to mark a member as former or not-current to remove from roster and featured member rotation.")

    class Meta: 
        ordering = ["instrument"]

    def __unicode__(self):
        return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)

    def get_absolute_url(self):
        return "/members/%i/" % self.id
    
class OrchestraMemberAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'last_name', 'first_name', 'instrument')
    list_filter = ('instrument',)

admin.site.disable_action('delete_selected')
admin.site.register(OrchestraMember, OrchestraMemberAdmin)
