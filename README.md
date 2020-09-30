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
* The remove option is still not implemented, but it will be. Still didn't need it so... Why it should be implemented xD. But i'm pretty sure that I will need it in the future so it will be implemented some day, hope near jajaja.