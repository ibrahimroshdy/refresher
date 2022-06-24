from celery import shared_task
from django.db.utils import IntegrityError
from loguru import logger

from apps.speedtester.models import ServersModel, SpeedtesterModel
from apps.speedtester.utils import RefresherSpeedtest


@shared_task
def process_speedtest():
    """
        A celery task that will be picked up.
        The task creates a speedtest instance and collects information of the conducted speedtest
        and adds them to the database using Django ORM.
    """
    refresher_speedtest = RefresherSpeedtest()
    speedtest_res = refresher_speedtest.get_speedtest()
    best = refresher_speedtest.get_best_server()
    servers = refresher_speedtest.get_servers()
    try:
        s = ServersModel.objects.create(**best)
        s.save()
    except IntegrityError as IE:
        logger.info(f"Best server {best['name']} exists. {IE}")

    _ = SpeedtesterModel.objects.update_or_create(best_server_id=int(best['id']), **speedtest_res)

    for item in servers:
        try:
            s = ServersModel.objects.create(**item)
            s.save()
        except IntegrityError as IE:
            logger.info(f"Server {item['name']} exists. {IE}")
