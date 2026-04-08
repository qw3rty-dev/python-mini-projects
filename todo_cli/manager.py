from utils import get_input,get_int
from datetime import datetime,date
HEADER=(f"\n{'Sno':<5} {'Status':<10} {'Task':<20} {'Priority':<10} {'Due Date [YYYY-MM-DD]':<12}")
DIVIDER= "-"*70

def print_tasks(tasks):
    print(HEADER)
    print(DIVIDER)
    for i,t in enumerate(tasks,1):
        tag= due_tag(t['due'])
        status = "[X]" if t["done"] else "[ ]"
        print(f"{i:<5} {status:<10} {t['task']:<20} {t['priority']:<10} {t['due']} {tag:<12}")



def add_task(tasks):                  

    task=get_input("Enter task: ",max_len=20)
    if task is None:
        return          
    
    if task in [t["task"].lower() for t in tasks]:
        print("Task already exists")
        return
    
    while True:
        priority = get_input("Priority (High/Medium/Low): ",allow_empty=True)
        if priority is None:
            return
        
        if priority in ["high","medium","low",'']:
            if priority=='':
                priority="low"
            break
        print("Invalid input | (High/Medium/Low) ")
        
    due=date_format("Enter due date (YYYY-MM-DD): ")
    if due is None:
        return

    tasks.append({"task":task.capitalize(),"done":False,"priority":priority.capitalize(),"due":due})
    print("Task added successfully")


def show_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return
    print_tasks(tasks)
    

def completed_tasks(tasks):
    completed=[x for x in tasks if x['done']]
    if len(completed)!=0:
        print("\n"+f"Completed Task{'s'if len(completed)!=1 else ''}".center(60))
        print_tasks(completed)
    else:
        print("No completed tasks")
        return
    

def pending_tasks(tasks):
    pending=[x for x in tasks if not x['done']]
    if len(pending)!=0:
        print("\n"+f"Pending Task{'s'if len(pending)!=1 else ''}".center(60))
        print_tasks(pending)
    else:
        print("No pending tasks")
        return
    

def mark_completed(tasks):
    show_tasks(tasks)
    while True:
        num=get_int("Enter the task number that you completed: ")
        print()
        if num is None:
            return
        if 1 <= num <= len(tasks):
            if tasks[num-1]["done"] != True:
                tasks[num-1]["done"] = True
                print("Task marked as completed")
            else:
                print("Already marked as completed")
            break
        else:
            print("Invalid task number,Please try again.")
            
    

def edit_tasks(tasks):

    show_tasks(tasks)
    num =get_int("\nEnter the task number to edit: ")
    print()
    if num is None:
        return
    
    if 1<= num <=len(tasks):
        toedit=tasks[num-1]
        new_name=get_input("Enter the new name for it [Leave it blank for no change]: ",allow_empty=True)
        if new_name is None:
            return

        while True:
            new_priority = get_input("Priority (High/Medium/Low or leave it blank for no change): ",allow_empty=True)
            if new_priority is None:
                return
            if new_priority in ["high","medium","low",'']:
                break
            print("Invalid input | (High/Medium/Low) ")
        new_due= date_format("Enter due date (YYYY-MM-DD) or leave it blank for no change: ",allow_empty=True)
        
        if new_due is None:
            return                    

        if new_name:
            toedit["task"]=new_name.capitalize()
        if new_priority:
            toedit["priority"]=new_priority.capitalize()
        if new_due:
            toedit["due"]=new_due

        if not new_name and not new_due and not new_priority:
            print("\nNo change is done")
        else:
            print("\nTask updated")
        
    else:
        print("Invalid task number,Please try again.")


def remove_task(tasks):
    if not tasks:
        print("No tasks available")
        return

    show_tasks(tasks)
    num=get_int("Enter the task number you want to remove: ")
    print()
    if num is None:
        return
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Task removed")
    else:
        print("Invalid task number,Please try again.")

    
def remove_completed(tasks):
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t["done"]]
    removed = before - len(tasks)
  
    if removed!=0:
        print(f"{removed} completed task{'s' if removed!=1 else ''} removed")
    else:
        print("No completed tasks to remove")


def search_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return
    word=get_input("Enter Keyword: ")
    if word is None:
        return
    results=[t for t in tasks if word.lower() in t['task'].lower()]
    if results:
         print_tasks(results)
    else:
        print("No matching tasks")


def sort_tasks(tasks):
    priority_order={'High':1,'Medium':2,'Low':3}
    sorted_tasks=sorted(tasks, key= lambda x:(datetime.strptime(x["due"],"%Y-%m-%d"),priority_order[x['priority']]))
    show_tasks(sorted_tasks)


def date_format(msg,allow_empty=False):
    while True:
        due= input(msg).strip().lower()
        if due == "cancel":
           return None
        if allow_empty and due=="":
            return ""
        try:
            date_str=datetime.strptime(due, "%Y-%m-%d")
            return date_str.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format")


def due_tag(due_date):
    today=date.today()
    due= datetime.strptime(due_date, "%Y-%m-%d").date()
    if today==due:
        return"(Today)"
    elif today>due:
        return"(Overdue)"
    else:
        return""
    

