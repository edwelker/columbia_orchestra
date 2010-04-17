from django.db import models
from django.contrib import admin
from ThumbnailImageField import ThumbnailImageField

# Create your models here.

class Instrument(models.Model):
    name = models.CharField(max_length=120)
    
    def __unicode__(self):
        return "%s" % self.name

class OrchestraMember(models.Model):  

    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)

    #instrument = models.IntegerField(max_length=10, choices=INSTRUMENTS)
    instrument = models.ForeignKey(Instrument)
    principal = models.BooleanField()

    bio = models.TextField(blank=True,help_text="Wrap paragraphs in '&lt;p&gt;...&lt;/p&gt;'")

    photo = ThumbnailImageField(blank=True,upload_to='images/user_photos')
    
    noncurrent_member = models.BooleanField(help_text="Use to mark a member as former or not-current to temporarily remove from roster.")

    class Meta: 
        ordering = ["instrument"]

    def __unicode__(self):
        return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)

    def get_absolute_url(self):
        return "/members/%i/" % self.id
    
class OrchestraMemberAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'last_name', 'first_name', 'instrument', 'principal', 'noncurrent_member')
    list_filter = ('instrument','principal','noncurrent_member')

admin.site.disable_action('delete_selected')
admin.site.register(Instrument)
admin.site.register(OrchestraMember, OrchestraMemberAdmin)
