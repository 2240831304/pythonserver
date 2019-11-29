
import readdataconsumer


objectPt = readdataconsumer.ReadDataConsumer()
# objectPt.daemon=True

flag = objectPt.connect_mq()
if flag:
    objectPt.start()

# objectPt.quit()