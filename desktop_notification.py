from plyer import notification
import time

def notify_me(title, message):
    notification.notify(
        title=title,
        message=message,
        # This is an example, you can use the same format for your directory where the icon is placed
        app_icon="C:\\Users\\User\\Documents\\Projects\\Desktop Notifier App\\eye-icon.ico",
        timeout=20,
    )

if __name__ == '__main__':
    while True:
        notify_me("Hello User, time for a break!", "It\'s time for 20-20-20 to keep your eyes healthy.")
        time.sleep(1200)
