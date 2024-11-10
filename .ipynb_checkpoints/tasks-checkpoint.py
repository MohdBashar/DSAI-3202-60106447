from celery import Celery

 # Configure Celery to use RabbitMQ as the message broker
# tasks.py or celeryconfig.py

from celery import Celery

app = Celery('tasks',
             broker='redis://10.102.0.106:6379/0',  # replace with your broker URL
             backend='redis://10.102.0.106:6379/0')  # result backend

@app.task
def power(n, power):
 return n ** power
