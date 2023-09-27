from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoTemplate.settings")

app = Celery("DjangoTemplate")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
