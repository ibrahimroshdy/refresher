import os

import django
import speedtest
from django.db.utils import IntegrityError
from loguru import logger

#Setup django to be able to access the settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.speedtester.models import ServersModel, SpeedtesterModel


class RefresherSpeedtest:
    def __init__(self):
        """
        A speedtest abstract class that iniates a speedtest method with catch clause for internet connection.
        """
        try:
            self.speedtester = speedtest.Speedtest()
        except speedtest.ConfigRetrievalError as CRE:
            logger.error(f'No internet connection: {CRE}')
            raise SystemExit

    def get_speedtest(self):
        """
        Speed test getter that translates bits to megabits
        Concanate all items into a struct or 'dict' for return
        :return:
        A dict containting download, upload, lat, lat of conducted speed test
        """
        lat_lon = self.speedtester.lat_lon
        return {
            'download': round(self.speedtester.download() * 10 ** -6, 3),
            'upload': round(self.speedtester.upload() * 10 ** -6, 3),
            'lat': lat_lon[0],
            'lon': lat_lon[1]
        }

    def get_best_server(self):
        """
        Get the best server that the speeed test is locked onto
        Added a new field called "Latency"
        :return:
        A dict with server information
        """
        best_server = self.speedtester.best
        return best_server

    def get_servers(self):
        """
        Converting a dict of list to a list of one item that is a list of dicts

        :return:
        List of server dicts that are within reach to the speedtest

        """
        servers = [i for i in [t for t in zip(*self.speedtester.servers.values())][0]]
        return servers


if __name__ == '__main__':
    refresher_speedtest = RefresherSpeedtest()
    speedtest_res = refresher_speedtest.get_speedtest()
    best = refresher_speedtest.get_best_server()
    servers = refresher_speedtest.get_servers()
    try:
        s = ServersModel.objects.create(**best)
        s.save()
    except IntegrityError as IE:
        logger.info(f"Best server {best['name']} exists. {IE}")

    speedtest_object = SpeedtesterModel.objects.update_or_create(best_server_id=int(best['id']), **speedtest_res)

    for item in servers:
        try:
            s = ServersModel.objects.create(**item)
            s.save()
        except IntegrityError as IE:
            logger.info(f"Server {item['name']} exists. {IE}")
