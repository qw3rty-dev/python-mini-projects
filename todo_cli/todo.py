import json
def main():
     tasks=load_tasks()
     while True:
         print(f"\nTotal tasks: {len(tasks)}")
         print(f"Completed:{len([x for x in tasks if x['done']])}")
         print(f"Pending:{len([x for x in tasks if not x['done']])}\n")
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
             break
         save_tasks(tasks)

             
def menu():
   print("===MENU===")
   print("1.) Add task\n"
       "2.) Show tasks\n"
       "3.) Mark as completed\n"
       "4.) Show pending tasks\n"
       "5.) Show completed tasks\n"
       "6.) Remove task\n"
       "7.) Remove all completed tasks\n" 
       "8.) Edit task\n"
       "9.) Search task\n"
       "10.) Exit\n")
   while True:
        choice = inputFN("Enter your choice: ")
        if 1 <= choice <= 10:
            return choice
        print("Choose between 1-9")

def add_task(tasks):                                     
    task=input("Enter task: ")
    
    if task.lower() in [t["task"].lower() for t in tasks]:
        print("Task already exists")
    else:
        while True:
            priority = input("Priority (High/Medium/Low): ").lower().strip()
            if priority in ["high","medium","low",'']:
                if priority=='':
                    priority="low"
                break
            print("Invalid input | (High/Medium/Low) ")

        tasks.append({"task":task.capitalize(),"done":False,"priority":priority.capitalize()})
        print("Task added")

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
    
    for i,t in enumerate(tasks):
        status = "✅" if t["done"] else "❌"
        print(f"{i+1}.) [{status}] {t['task']:<20} | Priority: {t['priority']}")



def completed_tasks(tasks):
    completed=[x for x in tasks if x['done']]
    if len(completed)!=0:
        print(f"=Completed Task{'s'if len(completed)!=1 else ''}=")
        for i,t in enumerate(completed):
            print(f"{i+1}.) {t['task']:<20} | Priority:{t['priority']}")
    else:
        print("No completed task(s)")
        return


def pending_tasks(tasks):
    pending=[x for x in tasks if not x['done']]
    if len(pending)!=0:
        print(f"=Pending Task{'s'if len(pending)!=1 else ''}=")
        for i,t in enumerate(pending):
            
            print(f"{i+1}.) {t['task']:<20} | Priority:{t['priority']}")
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
    if 1 <= num <= len(tasks):
        if tasks[num-1]["done"] != True:
            tasks[num-1]["done"] = True
            print("List updated")
        else:
            print("Already marked as completed")
    else:
        print("Invalid task number")
 

def edit_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return
    show_tasks(tasks)
    num =inputFN("Enter the task number to edit: ")
    print()
    if 1<= num <=len(tasks):
        toedit=tasks[num-1]

        new_name=input("Enter the new name for it: ")
        new_priority = input("Priority (High/Medium/Low or blank): ").lower()
        if new_priority:
            while new_priority not in ["high","medium","low"]:
                print("Invalid priority")
                new_priority = input("Enter High/Medium/Low: ").lower()

            toedit["priority"] = new_priority.capitalize()


        if new_name:
            toedit["task"]=new_name
        if new_priority:
            toedit["priority"]=new_priority.capitalize()
        print("Task updated")
    else:
        print("Invalid task number")



def remove_task(tasks):
    if not tasks:
        print("No tasks available")
        return

    show_tasks(tasks)
    
    num=inputFN("Enter the task number you want to remove: ")
    print()
    if 1 <= num <= len(tasks):
        tasks.pop(num-1)
        print("Task removed")
    else:
        print("Invalid task number")


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
    word=input("Enter Keyword: ").lower()
    found=False
    for i,t in enumerate(tasks):
        if word in t["task"].lower():
            status = "✅" if t["done"] else "❌"
            print(f"{i+1}.) [{status}] {t['task']:<20} | Priority: {t['priority']}")
            found=True
    if not found:
        print("No matching tasks")

    
def inputFN(msg):
    while True:
        try:
            x=int(input(msg))
            return x
        except ValueError:
            print("Invalid input")
            
if __name__=="__main__":
    main()
