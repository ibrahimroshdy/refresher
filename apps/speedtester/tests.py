from django.test import TestCase
from loguru import logger
from model_bakery import baker

from .models import ServersModel, SpeedtesterModel


# Create your tests here.
class ServersSpeeedTestCase(TestCase):
    def setUp(self):
        self.server = baker.make(ServersModel)
        self.speedtest = baker.make(SpeedtesterModel)

    def test_creation(self):
        if self.server and self.speedtest:
            logger.success('DB SUCCESS')
            assert True
        else:
            logger.error('DB ERROR')
            assert False

    def tearDown(self):
        ServersModel.objects.all().delete()
        SpeedtesterModel.objects.all().delete()
