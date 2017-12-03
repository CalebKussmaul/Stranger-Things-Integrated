#!/usr/bin/env python2
import stranger

import connexion
from gevent.wsgi import WSGIServer

if __name__ == '__main__':
    stranger.start_client()

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml', arguments={'title': 'Stranger board'})
    http_server = WSGIServer(('', 80), app)
    http_server.serve_forever()
