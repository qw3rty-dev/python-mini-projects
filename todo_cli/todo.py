import json
from datetime import datetime,date
HEADER=(f"\n{'Sno':<5} {'Status':<10} {'Task':<20} {'Priority':<10} {'Due Date':<12}")
DIVIDER= "-"*60
def main():
     tasks=load_tasks()
     
     while True:
         print("-"*120)
         print(f"\nTotal tasks: {len(tasks)}  |  Completed: {len([x for x in tasks if x['done']])}  | Pending: {len([x for x in tasks if not x['done']])}")
        
         choice=menu()
         if choice==1:
              add_task(tasks)
         elif choice==2:
             show_tasks(tasks)
         elif choice==3:
             mark_completed(tasks)
         elif choice==4:
             pending_tasks(tasks)
         elif choice==5:
             completed_tasks(tasks)
         elif choice==6:
             remove_task(tasks)
         elif choice==7:
             remove_completed(tasks)
         elif choice==8:
             edit_tasks(tasks)
         elif choice==9:
             search_tasks(tasks)
         elif choice==10:
             sort_tasks(tasks)
         elif choice==11:
             break
         save_tasks(tasks)

             
def menu():
   print("="*46 )
   print("\t\tTO-DO LIST MENU")
   print("="*46)
   print("[1] Add task\n"
       "[2] Show tasks\n"
       "[3] Mark as completed\n"
       "[4] Show pending tasks\n"
       "[5] Show completed tasks\n"
       "[6] Remove task\n"
       "[7] Remove all completed tasks\n" 
       "[8] Edit task\n"
       "[9] Search task\n"
       "[10] Sort tasks\n"
       "[11] Exit\n")
   print("Type 'cancel' anytime to go back to the menu\n")
   
   while True:
        choice = inputFN("Enter your choice: ")
        if choice is None:
            continue
        if 1 <= choice <= 11:
            return choice
        print("Choose between 1-11")
        

def add_task(tasks):                  
    task=get_input("Enter task: ",max_len=20)
    if task is None:
        return
    
    if task.lower() in [t["task"].lower() for t in tasks]:
        print("Task already exists")
        return
    
    while True:
        priority = get_input("Priority (High/Medium/Low): ",allow_empty=True)
        if priority is None:
            return
        priority=priority.strip().lower()
        
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

def save_tasks(tasks):                                              
    with open("tasks.json","w") as f:
        json.dump(tasks,f,indent=4)

def load_tasks():
    try:
        with open("tasks.json","r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return[]

        
def show_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return
    print_tasks(tasks)

def completed_tasks(tasks):
    completed=[x for x in tasks if x['done']]
    if len(completed)!=0:
        print(f"=Completed Task{'s'if len(completed)!=1 else ''}=")
        print_tasks(completed)
    else:
        print("No completed task(s)")
        return

def pending_tasks(tasks):
    pending=[x for x in tasks if not x['done']]
    if len(pending)!=0:
        print(f"=Pending Task{'s'if len(pending)!=1 else ''}=")
        print_tasks(pending)

    else:
        print("No pending task(s)")
        return
    

def mark_completed(tasks):
    if not tasks:
        print("No tasks available")
        return
    
    show_tasks(tasks)

    num=inputFN("Enter the task number that you completed: ")
    print()
    if num is None:
        return
    else:
        if 1 <= num <= len(tasks):
            if tasks[num-1]["done"] != True:
                tasks[num-1]["done"] = True
                print("Task marked as completed")
            else:
                print("Already marked as completed")
        else:
            print("Invalid task number,Please try again.")
    
 

def edit_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return
    show_tasks(tasks)
    num =inputFN("\nEnter the task number to edit: ")
    print()
    if num is None:
        return
    else:
        if 1<= num <=len(tasks):
            toedit=tasks[num-1]

            new_name=get_input("Enter the new name for it [Leave it blank for no change]: ",allow_empty=True)
            if new_name is None:
                return

            while True:
                new_priority = get_input("Priority (High/Medium/Low or leave it blank for no change): ",allow_empty=True)
                if new_priority is None:
                    return
                new_priority=new_priority.lower().strip()
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
    
    num=inputFN("Enter the task number you want to remove: ")
    print()
    if num is None:
        return
    else:
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

    
def inputFN(msg):
    while True:
        try:
            x=input(msg)
            if x.lower()=="cancel":
                return
            else:
              x=int(x)
              return x
        except ValueError:
            print("Invalid input,Please try again")

def date_format(msg,allow_empty=False):
    while True:
        due= input(msg).strip()
        if due.lower()=="cancel":
           return None
        if allow_empty and due=="":
            return ""
        try:
            date_str=datetime.strptime(due, "%Y-%m-%d")
            return date_str.strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format")

def sort_tasks(tasks):
    priority_order={'High':1,'Medium':2,'Low':3}
    sorted_tasks=sorted(tasks, key= lambda x:(datetime.strptime(x["due"],"%Y-%m-%d"),priority_order[x['priority']]))
    show_tasks(sorted_tasks)

def due_tag(due_date):
    today=date.today()
    due= datetime.strptime(due_date, "%Y-%m-%d").date()
    if today==due:
        return"(Today)"
    elif today>due:
        return"(Overdue)"
    else:
        return""
    
def print_tasks(tasks):
    print(HEADER)
    print(DIVIDER)
    for i,t in enumerate(tasks,1):
        tag= due_tag(t['due'])
        status = "[X]" if t["done"] else "[ ]"
        print(f"{i:<5} {status:<10} {t['task']:<20} {t['priority']:<10} {t['due']} {tag:<12}")

def get_input(msg,allow_empty=False,max_len=None):
    while True:
        value= input(msg).strip()
        if value.lower() == "cancel":
            return None
        if not value and not allow_empty:
            print("Input can't be empty")
            continue
        if max_len and len(value)> max_len:
            print(f"Keep it under {max_len} characters")
            continue
        return value

if __name__=="__main__":
    main()
