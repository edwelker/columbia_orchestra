from orch.meet_the_orchestra.models import OrchestraMember
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def home(request):
    m = OrchestraMember.objects.all()[0] #will be changed be randomized later
    
    return render_to_response('home.html', {'member': m}, context_instance=RequestContext(request))