
import readdataconsumer
import os
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

