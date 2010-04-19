from orch.events.models import Season, Event, Location, Soloist, PreConcertDiscussion
from django.contrib import admin

class SeasonAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('name', 'startdate', 'enddate', 'description')

admin.site.register(Season, SeasonAdmin)

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('name', 'city', 'zip')
    
admin.site.register(Location, LocationAdmin)

class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('name', 'date', 'location', 'season')
    list_filter = ('location',)
    

admin.site.register(Event, EventAdmin)

class PreConcertDiscussionAdmin(admin.ModelAdmin):
    pass

admin.site.register(PreConcertDiscussion)

class SoloistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['name']}
    list_display = ('name', 'instrument', 'work')
    list_filter = ('instrument',)

admin.site.register(Soloist, SoloistAdmin)
