import schedule
import time
import psutil
# import pynotifier
from plyer import notification

batarydata=psutil.sensors_battery()
def notify():
    
    # print(batarydata.percent)

    if batarydata.percent == 90:
        print("plug out")
        notification.notify(
        title="Battery Percentage",
        message=str(batarydata.percent)+"% Battery remaining",
        timeout=10
        )
        time.sleep(6)
    
    else:
        print("plug in")
        pass

while True:
 
    # Checks whether a scheduled task
    # is pending to run or not

    notify()
    schedule.run_pending()
    # if batarydata.percent>60:
    #     break

    time.sleep(1)
    
    



