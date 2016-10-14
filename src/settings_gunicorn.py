from __future__ import unicode_literals

import multiprocessing
import os

APP_ENV = os.environ.get('APP_ENV', 'training')

bind = '0.0.0.0:8001'
workers = multiprocessing.cpu_count() * 2 + 1
errorlog = accesslog = '-'
loglevel = 'info'
preload_app = True
proc_name = 'simple-app-' + APP_ENV
