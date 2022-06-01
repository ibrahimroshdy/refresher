# Create your tasks here
from apps.speedtester.models import ServersModel, SpeedtesterModel
from apps.speedtester.utils import RefresherSpeedtest
from celery import shared_task


@shared_task
def process_speedtest():
    refresher_speedtest = RefresherSpeedtest()
    speedtest_res = refresher_speedtest.get_speedtest()
    best = refresher_speedtest.get_best_server()
    # servers = refresher_speedtest.get_servers()
    # print(f'{servers}')

    server_object = ServersModel.objects.create(**best)
    _ = SpeedtesterModel.objects.create(**speedtest_res, best_server_id=server_object.id)
    # server_objs = ServersModel.objects.bulk_create(servers)
