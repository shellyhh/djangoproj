#-*- coding:utf8 -*-
from __future__ import absolute_import

import os

from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINS_MODULE', 'attproj.settings')
app = Celery('attproj')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print ('Request: {0!r}'.format(self.request))
