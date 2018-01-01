CELERY_IMPORTS = ('tasks')
CELERY_IGNORE_RESULT = False
BROKER_HOST = '10.5.50.95'
BROKER_PORT = 5672
BROKER_URL= 'amqp://'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
	'doctor-every-10-seconds':{
        'task' : 'task.fav_doctor',
        'schedule' : timedelta(seconds=10),
    },
}