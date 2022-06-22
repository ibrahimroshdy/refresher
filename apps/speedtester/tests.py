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
        """
        Tests database creation
        :return: True if a server and speedtest instances were created sucessfully.
        """
        if self.server and self.speedtest:
            logger.success('DB SUCCESS')
            logger.info(f'{self.server.__str__()})')
            logger.info(f'{self.speedtest.__str__()})')
            assert True

    def test_process_speedtest(self):
        """
        Processess a speedtest that gets the result, best server, and the pinged servers.
        :return: True if the speedtest is processed and no errors happened.
        """
        speedtest_res, best, servers = process_speedtest_test()
        if speedtest_res:
            logger.success(speedtest_res)
            logger.success(best)
            assert True

    def tearDown(self):
        ServersModel.objects.all().delete()
        SpeedtesterModel.objects.all().delete()
