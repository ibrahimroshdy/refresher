from django.db import models
from model_utils.models import TimeStampedModel


class ServersModel(TimeStampedModel):
    id = models.IntegerField('id', primary_key=True)
    url = models.URLField('url')
    lat = models.FloatField('lat')
    lon = models.FloatField('lon')
    name = models.CharField('city', max_length=256)
    country = models.CharField('country', max_length=256)
    cc = models.CharField('country code', max_length=5)
    sponsor = models.CharField('sponsor', max_length=256)
    host = models.CharField('host', max_length=256)
    d = models.FloatField('d')
    latency = models.FloatField('latency', null=True, blank=True)

    def __str__(self):
        return f'{self.cc}.{self.name}'

    class Meta:
        verbose_name = 'Server'
        verbose_name_plural = 'Servers'


class SpeedtesterModel(TimeStampedModel):
    best_server = models.ForeignKey(ServersModel, on_delete=models.CASCADE)
    download = models.FloatField('download')
    upload = models.FloatField('upload')
    lat = models.FloatField('lat')
    lon = models.FloatField('lon')

    def __str__(self):
        return f'{self.best_server.cc}.{self.best_server.name}: [{self.download}]'

    class Meta:
        verbose_name = 'Speed Test'
        verbose_name_plural = 'Speed Tests'
