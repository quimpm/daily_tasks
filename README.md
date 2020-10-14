# Task Manager

I made this "Task Manager" as a local Agenda for my daily organitzation.

## Installation

Write into the comand line:
```bash
vim ~/.bash_aliases
```
Append to the file:
```bash
alias addtask='python3 /path/to/your/containing/dir/addtask.py'
alias tasks='/path/to/your/containing/dir/display.sh'
alias removetask='python3 /path/to/your/containing/dir/remove_task.py'
```
Save and close the file and activate your alias typing:
```bash
source ~/.bash_aliases
```
Also I've made a cron that runs every 10 minutes and notifies you every 10 minuts 30 minutes before the task has to be done.
Type into de comand line crontab -e and then put into the PENULTIMATE line of the file this line:
```bash 
*/10 * * * *    /home/quimpm/stuff/tasks_manager/gui-launcher.sh "/path/to/your/containing/dir/notify.sh"
```

## Usage:
* To add a task write addtask
* To see the tasks you can make it in diferent ways:
    * tasks : This will show the tasks u have in the next 24h
    * tasks <number>: This will show the tasks u have in the next <number> days
    * tasks <dd-mm-YYYY>: This will show the tasks you have the <dd-mm_YYYY>
* To remove a task type removetask, next the program will ask you for the id of the task you want to remove.