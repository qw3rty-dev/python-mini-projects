import json
import os

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
    
def clear():
    os.system("cls" if os.name=="nt" else "clear")

def get_int(msg):
    while True:
        try:
            x=input(msg).strip()
            if x.lower()=="cancel":
                return None
            else:
              x=int(x)
              return x
        except ValueError:
            print("Please enter a valid numeric value")



def get_input(msg,allow_empty=False,max_len=None):
    while True:
        value= input(msg).strip().lower()
        if value == "cancel":
            return None
        if not value and not allow_empty:
            print("Input can't be empty")
            continue
        if max_len and len(value)> max_len:
            print(f"Keep it under {max_len} characters")
            continue
        return value


