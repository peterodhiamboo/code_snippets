# This is a script to add, remove update or delete tasks
import datetime
import random
import uuid
import json
import io
import os


e = datetime.datetime.now()


date_time_creation = e.strftime("%Y-%m-%d %H:%M:%S")

my_tasks = []

def where_json(file_name):
    return os.path.exists(file_name)

if where_json('data.json'):
    pass
else:
    with open('data.json', 'w') as outfile:  
        json.dump(my_tasks, outfile)


def beginner():
    #storing the data into json file
    #This option cecks if the json file exists and craetes one if none exists

    print('Hello, welcome to the CLI todo list app \n please select an option to proceed \n 1. To add tasks \n 2. To update tasks \n')
    choice_selection = int(input('Enter the selection here : '))
    
    if choice_selection == 1:
        add_task()
    elif choice_selection == 2:
        unique_identifier = input('Enter the UID of the task to be edited : ')
        update_task(unique_identifier)
    elif choice_selection == 3:
        view_tasks()
        

def add_task():

    task_to_be_added = input ('Enter a task you wat to add :')
    added_task = task_to_be_added + ': ' + date_time_creation
    unique_task_identifier = str(uuid.uuid4())

    # CALL THE METHOD TO CHECK IF JSON EXISTS
    where_json('data.json')

    #read contents of json file
    #this code segment has to be here so that mytask can be appended on the already existing list, 
    #without this, the code will writing on file instead of appending
    with open('data.json') as fp:
        my_tasks = json.load(fp)

    my_tasks.append(
        {
            'uid' : unique_task_identifier,
            'task': task_to_be_added,
            'the_date_created': date_time_creation
        }
    )

    #dumping data to the json (tasks)
    with open('data.json', 'w') as json_file:
        json.dump(my_tasks, json_file, 
                        indent=4,  
                        separators=(',',': '))

    print('Task creation successful')


def update_task(task_uid):
    with open("data.json", "r") as read_file:
        data = json.load(read_file)

        for k in data:
            print(k)


def view_tasks():
    i = 0
    with open("data.json", "r") as read_file:
        data = json.load(read_file)

        for j in data:
            print(j)
            i+=1
    
beginner()