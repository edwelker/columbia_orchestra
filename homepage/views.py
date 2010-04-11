from orch.meet_the_orchestra.models import OrchestraMember
from orch.homepage.models import Event
from django.template import RequestContext
from django.shortcuts import render_to_response
import datetime

# Create your views here.

def home(request):
    m = OrchestraMember.objects.all() #will be changed be randomized later
    e = Event.objects.filter(date__gte=datetime.datetime.today()).order_by("date")
        
    event = e[0] if (len(e) > 0) else None
    member = m[0] if (len(m) > 0) else None
    
    return render_to_response('home.html', {'member': member, 'event': event}, 
                              context_instance=RequestContext(request))