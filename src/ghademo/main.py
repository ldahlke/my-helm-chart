import os
import time
import random
import logging
from typing import Optional

from prometheus_client import start_http_server, Gauge, Summary

TIMEINTERVAL_SEC = 60
PROMETHEUS_PORT = 9000

global_logger = logging.getLogger(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    global_logger.info(f'Sleeping for {t} seconds...')
    time.sleep(t)
    time.sleep(t)

def main():
    logging.basicConfig(level=10)  # override locust logging config
    start_http_server(PROMETHEUS_PORT)
    global_logger.info('Starting demo ...')
    while True:
        process_request(random.random())

if __name__ == '__main__':
    main()
