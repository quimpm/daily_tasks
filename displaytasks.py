from TaskManager import TaskManager
from datetime import date, datetime
from time import strptime
import re
import sys

def write_html_file(tasks, day):
    html = open('display.html','w')
    html.write('<!DOCTYPE html>')
    html.write('<html lang="en">')
    html.write('<head>')
    html.write('<meta charset="UTF-8">')
    html.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
    html.write('<title>Today Tasks</title>')
    html.write('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">')
    html.write('<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>')
    html.write('<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>')
    html.write('<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>')
    html.write('</head>')
    html.write('<body>')
    html.write('<div class="container">')
    html.write('<div class="col-xs-12" align="center">')
    html.write('<div class="list-group">') 
    html.write('<h3>'+day+'</h3>')
    for item in tasks:
        if datetime.fromtimestamp(item['datetime']).strftime("%d-%m-%Y") != day:
            html.write('<h3>'+datetime.fromtimestamp(item['datetime']).strftime("%d-%m-%Y")+'</h3>')
            day = datetime.fromtimestamp(item['datetime']).strftime("%d-%m-%Y")
        html.write('<a href="#" class="list-group-item list-group-item-action">')
        html.write('<div class="d-flex w-100 justify-content-between">')
        html.write('<h5 class="mb-1">'+item['title']+'</h5>')
        html.write('<small>'+datetime.fromtimestamp(item['datetime']).strftime("%h-%m-%s")+'</small>')
        html.write('</div>')
        html.write('<p class="mb-1">'+item['description']+'</p>')
        html.write('</a>')
    html.write('</div>')
    html.write('</div>')
    html.write('</div>')
    html.write('</body>')
    html.write('</html>')
 

def main():
    day = date.today().strftime("%d-%m-%Y")
    if len(sys.argv) == 1:
        tasks = sorted(TaskManager.getDayTasks(datetime.today().timestamp()), key = lambda x : x['datetime'])
    elif len(sys.argv) == 2:
        if re.search('^([0-2][0-9]|(3)[0-1])(\-)(((0)[0-9])|((1)[0-2]))(\-)\d{4}$',sys.argv[1]):
            date_in_sec = datetime.strptime(sys.argv[1]+' 00:00:00', "%d-%m-%Y %H:%M:%S").timestamp()
            day = datetime.fromtimestamp(date_in_sec).strftime("%d-%m-%Y")
            tasks = sorted(TaskManager.getDayTasks(date_in_sec), key = lambda x : x['datetime'])
        elif re.search('^[0-9]*$',sys.argv[1]):   
            tasks = sorted(TaskManager.getVariableDayTasks(int(sys.argv[1])), key = lambda x : x['datetime'])
        else:
            print('Usage: tasks [optional]<Nº of days forward from today> or <Exact day date dd-mm-yyyy format>')
            exit(-1)
    else:
        print('Usage: tasks [optional]<Nº of days forward from today> or <Exact day date dd-mm-yyyy format>')
        exit(-1)
    write_html_file(tasks,day)
 
if __name__ == "__main__":
    main()