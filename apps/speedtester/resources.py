from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from . import models


class SpeedtesterResource(resources.ModelResource):
    id = fields.Field(attribute='id')
    best_server = fields.Field(attribute='best_server', widget=ForeignKeyWidget(models.ServersModel, 'url'))

    class Meta:
        model = models.SpeedtesterModel
