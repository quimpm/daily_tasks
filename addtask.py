from Task import Task
from TaskManager import TaskManager
from datetime import datetime

def get_task():
    date_time = input('Enter a day and hour in dd-mm-yyyy hh:mm:ss format: ')
    date_time = datetime.strptime(date_time, "%d-%m-%Y %H:%M:%S").timestamp()
    title = input('Enter a title: ')
    description = input('Enter a description: ')
    return Task.Builder().addDatetime(date_time).addTitle(title).addDescription(description).build()

def main():
    task = get_task()
    TaskManager.addTask(task)

if __name__ == "__main__":
    main()