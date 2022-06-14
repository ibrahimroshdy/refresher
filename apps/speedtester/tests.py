from django.test import TestCase
from loguru import logger
from model_bakery import baker

from .models import ServersModel, SpeedtesterModel
from .utils import process_speedtest_test


# Create your tests here.
class ServersSpeeedTestCase(TestCase):
    def setUp(self):
        self.server = baker.make(ServersModel)
        self.speedtest = baker.make(SpeedtesterModel)

    def test_creation(self):
        if self.server and self.speedtest:
            logger.success('DB SUCCESS')
            logger.info(f'{self.server.__str__()})')
            logger.info(f'{self.speedtest.__str__()})')
            assert True

    def test_process_speedtest(self):
        speedtest_res, best, servers = process_speedtest_test()
        if speedtest_res:
            logger.success(speedtest_res)
            logger.success(best)
            assert True

    def tearDown(self):
        ServersModel.objects.all().delete()
        SpeedtesterModel.objects.all().delete()
