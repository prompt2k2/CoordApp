from import_export import resources
from .models import Sites

class SitesResource(resources.ModelResource):
    class Meta:
        model = Sites