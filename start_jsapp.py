from gevent import monkey
monkey.patch_all()

import argparse
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
from jumpserver.wsgi import application
import os

version = '1.0.0'

root_path = os.path.dirname(__file__)

parser = argparse.ArgumentParser(description="jsapp - 基于WebSocket的SSH堡垒机")
parser.add_argument('--port', '-p',
                    type=int,
                    default=8000,
                    help='服务器端口，默认为8000')

parser.add_argument('--host', '-H',
                    default='0.0.0.0',
                    help='服务器IP，默认为0.0.0.0')

args = parser.parse_args()

print('\033[31mJsApp\033[0m {0}  running on  {1} : {2}'.format(version, args.host, args.port))

ws_server = WSGIServer(
    (args.host, args.port),
    application,
    log=None,
    handler_class=WebSocketHandler
)

try:
    ws_server.serve_forever()
except KeyboardInterrupt:
    print('服务器关闭......')
    pass
