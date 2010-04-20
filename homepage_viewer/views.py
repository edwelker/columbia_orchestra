from orch.roster.models import OrchestraMember
from orch.events.models import Event
from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime
import random
from django.core.cache import cache

# Create your views here.

def home(request):
    '''get an event and member to display on the homepage. objects cached for an hour'''
    
    member = cache.get('member')
    primary_event = cache.get('primary_event')
    secondary_event = cache.get('secondary_event')
    
    if member and primary_event and secondary_event:
        return render_to_response('home.html', {'member': member, 'primary_event': primary_event, 'secondary_event': secondary_event}, 
                              context_instance=RequestContext(request))
    
    m = OrchestraMember.objects.exclude(photo__exact="").exclude(noncurrent_member=True).exclude(bio__exact="")
    if len(m) > 0:
        rand_index = random.randint(0, (len(m) -1 ))
        member = m[rand_index] if (len(m) > 0) else None
    
    #Status=1: Primary Event
    e = Event.objects.filter(date__gte=datetime.datetime.today()).filter(status=1).order_by("date")
    primary_event = e[0] if (len(e) > 0) else None
    
    #Status=2: Secondary Event
    ee = Event.objects.filter(date__gte=datetime.datetime.today()).filter(status=2).order_by("date")
    secondary_event = ee[0] if (len(ee) > 0) else None
    
    #set for the hour
    cache.set('member', member, 3600)
    cache.set('primary_event', primary_event, 3600)
    cache.set('secondary_event', secondary_event, 3600)
    
    return render_to_response('home.html', {'member': member, 'primary_event': primary_event, "secondary_event": secondary_event}, 
                              context_instance=RequestContext(request))
    
