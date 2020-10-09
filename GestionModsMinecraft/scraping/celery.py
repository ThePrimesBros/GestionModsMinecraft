from __future__ import absolute_import
import os
from celery import Celeryfrom celery.schedules import crontab # scheduler# default django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_web_scraping_example.settings')
app = Celery('django_web_scraping_example')
app.conf.timezone = 'UTC'
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()