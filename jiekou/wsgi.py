"""
WSGI config for jiekou project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from os.path import join,dirname,abspath

PROJECT_DIR = dirname(dirname(abspath(__file__)))#3
import sys # 4
sys.path.insert(0,PROJECT_DIR) # 5

os.environ['HTTPS'] = "on"

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jiekou.settings")

application = get_wsgi_application()



from readrecord.rabbitmq import readdataconsumer
import signal


pid = os.fork()
if  pid == 0:

    objectPt = readdataconsumer.ReadDataConsumer()
    signal.signal(signal.SIGINT, objectPt.signalQuit)
    flag = objectPt.connect_mq()
    if flag:
        objectPt.startConsumer()
else:
    print("parent process ID:%d,main process ID:%d" % (os.getpid(),os.getppid()) )

