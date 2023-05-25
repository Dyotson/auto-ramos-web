***REMOVED***
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autoramosweb.settings'***REMOVED***

app = Celery('autoramosweb'***REMOVED***

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY'***REMOVED***

# Load task modules from all registered Django apps.
app.autodiscover_tasks(***REMOVED***


@app.task(bind=True***REMOVED***
def debug_task(self***REMOVED***:
    print(f'Request: {self.request!r***REMOVED***'***REMOVED***


app.conf.beat_schedule = {
    # Execute the Speed Test every 10 minutes
    'revalidar-cookie-10min': {
        'task': 'revalidar_cookie',
        'schedule': crontab(minute='*/10'***REMOVED***,
        # 'schedule': crontab(***REMOVED***,
***REMOVED***
***REMOVED***
