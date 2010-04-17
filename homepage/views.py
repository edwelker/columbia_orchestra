from orch.meet_the_orchestra.models import OrchestraMember
from orch.homepage.models import Event
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
    
    m = OrchestraMember.objects.exclude(photo__exact="", former_member="True")
    if len(m) > 0:
        rand_index = random.randint(0, (len(m) -1 ))
        member = m[rand_index] if (len(m) > 0) else None
    
    e = Event.objects.filter(date__gte=datetime.datetime.today()).order_by("date")
    event = e[0] if (len(e) > 0) else None
    
    #set for the hour
    cache.set('member', member, 0)
    cache.set('event', event, 0)
    
    return render_to_response('home.html', {'member': member, 'event': event}, 
                              context_instance=RequestContext(request))
    