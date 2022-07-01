import os
import time
import logging
from typing import Optional

from prometheus_client import start_http_server, Gauge

TIMEINTERVAL_SEC = 300
PROMETHEUS_PORT = 9000
DEBUG_LEVEL = logging.DEBUG_LEVEL


global_logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=DEBUG_LEVEL)  # override locust logging config
    start_http_server(PROMETHEUS_PORT)
    # Stay with a list if multiple hosts should run
    while True:
        global_logger.info('Starting demo ...')
        remaining_sleep = TIMEINTERVAL_SEC - (time.time() - start_time)
        if remaining_sleep > 0:
            global_logger.info(f'Sleeping for {remaining_sleep} seconds...')
            time.sleep(remaining_sleep)

if __name__ == '__main__':
    main()
