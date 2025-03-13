from celery import Celery
import os

# Set up Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sendify.settings')
app = Celery('sendify')

# Load configuration from Django settings

app.config_from_object('django.conf:settings', namespace='CELERY')

# Register Celery tasks from all apps

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')