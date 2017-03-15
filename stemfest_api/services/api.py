from tastypie.resources import ModelResource
from services.models import Activity

class ActivityResource(ModelResource):
  class Meta:
    queryset=Activity.objects.all()
    resource_name='activity'
    allowed_methods=['get']