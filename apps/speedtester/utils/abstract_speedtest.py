import os

import django
import speedtest
from loguru import logger

#Setup django to be able to access the settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.speedtester.models import ServersModel, SpeedtesterModel


class RefresherSpeedtest:
    def __init__(self):
        try:
            self.speedtester = speedtest.Speedtest()
        except speedtest.ConfigRetrievalError as CRE:
            logger.error(f'No internet connection')
            raise SystemExit

    def get_speedtest(self):
        lat_lon = self.speedtester.lat_lon
        return {
            'download': round(self.speedtester.download() * 10 ** -6, 3),
            'upload': round(self.speedtester.upload() * 10 ** -6, 3),
            'lat': lat_lon[0],
            'lon': lat_lon[1]
        }

    def get_best_server(self):
        best = self.speedtester.best
        best.pop('id')
        return best

    # def get_servers(self):
    #     servers = []
    #     for i, item in enumerate(self.speedtester.servers):
    #         for j in item:
    #             j.pop('id')
    #             servers.append(j)
    #     return servers


if __name__ == '__main__':
    refresher_speedtest = RefresherSpeedtest()
    speedtest_res = refresher_speedtest.get_speedtest()
    best = refresher_speedtest.get_best_server()
    # servers = refresher_speedtest.get_servers()
    # print(f'{servers}')

    server_object = ServersModel.objects.create(**best)
    speedtest_object = SpeedtesterModel.objects.create(**speedtest_res, best_server_id=server_object.id)
    # server_objs = ServersModel.objects.bulk_create(servers)
