import time
from celery import shared_task

@shared_task
def test_task():
    print('Celery Started...........................')
    time.sleep(30)
    print('Celery Finished...........................')