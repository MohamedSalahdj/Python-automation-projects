import os
from plyer import notification

os.chdir(os.path.dirname(os.path.abspath(__file__))) # to change current working directory with this opened file 
print(os.getcwd())

notification.notify(
    title = 'Notification',
    message = 'this is the first notification from python program',
    app_icon = r'notification-icon.ico', # you must have notification-icon.ico in current working directory or will raise an error 
    timeout = 15,
)