"""gunicorn server config"""
from multiprocessing import cpu_count
from os import environ


def max_workers():
    return cpu_count()


# bind = '0.0.0.0:' + environ.get('POST', '8000')
bind = '0.0.0.0:8000'

max_requests = 10000
worker_class = 'sync'
workers = max_workers()
