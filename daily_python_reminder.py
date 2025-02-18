from plyer import notification
import time

def main():
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == "15:50:00": # Set time
            send_notification()
            time.sleep(86400)

def send_notification():
    notification_title = "Python Learning Reminder"
    notification_message = "Time to work on your Python learning!"

    notification.notify(
        title=notification_title,
        message=notification_message,
        timeout=10 # Duration in seconds
    )
    

if __name__ == "__main__":
    send_notification()