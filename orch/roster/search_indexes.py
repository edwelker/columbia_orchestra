from haystack.indexes import *
from haystack import site
from orch.roster.models import OrchestraMember

class OrchestraMemberIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    first_name = CharField(model_attr='first_name')
    middle_name = CharField(model_attr='middle_name')
    last_name = CharField(model_attr='last_name')
    bio = CharField(model_attr='bio')
    
    def get_queryset(self):
        """Used when the entire index for model is updated."""
        return OrchestraMember.objects.all()
    
site.register(OrchestraMember, OrchestraMemberIndex)
    