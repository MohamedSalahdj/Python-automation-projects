import os
import time
import schedule
from plyer import notification

os.chdir(os.path.dirname(os.path.abspath(__file__)))
def pomodoro_notification():
    notification.notify (
        title = 'Pomodoro Technique',
        message = 'You must take a rest now',
        app_icon = 'pomodoro-technique.ico',
        timeout = '300', # this notification will appear for 300 seconds (5 minutes)
    )

schedule.every(25).minutes.do(pomodoro_notification) # you can change this period '25' to any period of time 

while True:
    schedule.run_pending()
    time.sleep(300)

