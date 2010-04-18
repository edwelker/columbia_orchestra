from orch.roster.models import OrchestraMember
from orch.season.models import Event
from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime
import random
from django.core.cache import cache

# Create your views here.

def home(request):
    '''get an event and member to display on the homepage. objects cached for an hour'''
    
    member = cache.get('member')
    event = cache.get('event')
    
    if member and event:
        return render_to_response('home.html', {'member': member, 'event': event}, 
                              context_instance=RequestContext(request))
    
    m = OrchestraMember.objects.exclude(photo__exact="").exclude(noncurrent_member=True).exclude(bio__exact="")
    if len(m) > 0:
        rand_index = random.randint(0, (len(m) -1 ))
        member = m[rand_index] if (len(m) > 0) else None
    
    e = Event.objects.filter(date__gte=datetime.datetime.today()).order_by("date")
    event = e[0] if (len(e) > 0) else None
    
    #set for the hour
    cache.set('member', member, 3600)
    cache.set('event', event, 3600)
    
    return render_to_response('home.html', {'member': member, 'event': event}, 
                              context_instance=RequestContext(request))
    
