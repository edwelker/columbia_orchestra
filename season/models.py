from django.db import models
from django.contrib import admin

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the Event. Must be unique, even across seasons (so if you're doing 'Holiday Concert', make it '2009 Holiday Concert', etc.)")
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    #location = models.ForeignKey(Location)
    ticket_link = models.URLField( blank=True, null=True, help_text="Link to purchase tickets online.")
    #season = models.ForeignKey(Season)
    description = models.TextField(help_text="Description paragraphs (required). Please wrap all paragraphs in '&lt;p&gt;....&lt;/p&gt;'.")    
    slug = models.SlugField(unique=True, help_text='Suggested value is automatically generated from event name. Must be unique.')
    #soloists = models.ManyToManyField("Soloist")
    image = models.ImageField( help_text="Select a image to represent this concert.", upload_to="images")

    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ["date"]
        
    def get_absolute_url(self):
        return "/events/%s/" % self.slug

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}

admin.site.register(Event, EventAdmin)
