import os

import django

# Setup django to be able to access the settings file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'refresher_config.settings')
django.setup()

from .abstract_speedtest import RefresherSpeedtest


def process_speedtest_test():
    """

    :return:
    """
    refresher_speedtest = RefresherSpeedtest()
    speedtest_res = refresher_speedtest.get_speedtest()
    best = refresher_speedtest.get_best_server()
    servers = refresher_speedtest.get_servers()
    client = refresher_speedtest.get_client()

    return speedtest_res, best, servers, client

