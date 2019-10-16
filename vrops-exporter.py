import sys
import time
import os
from prometheus_client import start_http_server
from module.YamlRead import YamlRead
from module.VropsCollector import VropsCollector

if __name__ == '__main__':
    # Read yaml file
    config = YamlRead(sys.argv[1]).run()
    os.environ['USER'] = config['user']
    os.environ['PASSWORD'] = config['password']

    # Debug option
    os.environ['DEBUG'] = '0'
    if config['debug'] is True:
        os.environ['DEBUG'] = '1'print(os.environ['DEBUG'])

    # Start the Prometheus http server.
    start_http_server(config['port'])

    while True:
        time.sleep(1)

