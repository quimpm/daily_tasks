from TaskManager import TaskManager

def removeTask():
    taskID = input('Enter a id of the task you want to delete: ')
    TaskManager.removeTask(int(taskID))

def main():
    removeTask()

if __name__ == "__main__":
    main()