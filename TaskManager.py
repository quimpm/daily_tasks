from tinydb import TinyDB, Query
from datetime import date, timedelta, datetime
from time import strptime

class TaskManager():

    db = TinyDB('/home/quimpm/stuff/tasks_manager/db.json')
    Task = Query()

    @staticmethod
    def addTask(task):
        TaskManager.db.insert(task.asdict())

    @staticmethod
    def removeTask(task):
        pass

    @staticmethod
    def getDayTasks(day):
        today_tasks = TaskManager.db.search((TaskManager.Task.datetime >= day) & (TaskManager.Task.datetime <= (day + 86400)))
        return today_tasks

    @staticmethod
    def getVariableDayTasks(n_days):
        today = datetime.today().timestamp()
        end_day = (datetime.today() + timedelta(days=n_days)).timestamp()
        tasks = TaskManager.db.search((TaskManager.Task.datetime >= today) & (TaskManager.Task.datetime <= end_day))
        return tasks

    @staticmethod
    def getInmediateTasks():
        today = datetime.today().timestamp()
        inmediate_tasks = TaskManager.db.search((TaskManager.Task.datetime >= today) & (TaskManager.Task.datetime <= (today + 1800)))
        return inmediate_tasks

    @staticmethod
    def removeTask(taskID):
        TaskManager.db.remove(doc_ids=[taskID])