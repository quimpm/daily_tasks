from TaskManager import TaskManager
from datetime import datetime

import subprocess

def sendmessage(message):
    subprocess.Popen(['/usr/bin/notify-send', message])

def main():
    tasks = TaskManager.getInmediateTasks()
    for task in tasks:
        sendmessage(task["title"]+' at '+datetime.fromtimestamp(task['datetime']).strftime("%H:%M:%S"))


if __name__ == "__main__":
    main()
