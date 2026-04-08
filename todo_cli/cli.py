import manager as mg
from utils import load_tasks,save_tasks,get_int,clear


def menu(tasks):
   

   print(f"\nTotal tasks: {len(tasks)}  |  Completed: {len([x for x in tasks if x['done']])}  | Pending: {len([x for x in tasks if not x['done']])}")
   print("="*70 )
   print("TO-DO LIST MENU".center(70))
   print("="*70)
   print("[1]  Add task\n"
       "[2]  Show tasks\n"
       "[3]  Mark as completed\n"
       "[4]  Show pending tasks\n"
       "[5]  Show completed tasks\n"
       "[6]  Remove task\n"
       "[7]  Remove all completed tasks\n" 
       "[8]  Edit task\n"
       "[9]  Search task\n"
       "[10] Sort tasks\n"
       "[11] Exit\n")
   print("Type 'cancel' anytime to go back to the menu\n")
   
   while True:
        choice = get_int("Enter your choice: ")
        if choice is None:
            continue
        if 1 <= choice <= 11:
            return choice
        print("Choose between 1-11")


def main():
     tasks=load_tasks()
     
     while True:
         clear()
         choice=menu(tasks)
         if choice==1:
             mg.add_task(tasks)
             save_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==2:
             mg.show_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==3:
             mg.mark_completed(tasks)
             save_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==4:
             mg.pending_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==5:
             mg.completed_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==6:
             mg.remove_task(tasks)
             save_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==7:
             mg.remove_completed(tasks)
             save_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==8:
             mg.edit_tasks(tasks)
             save_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==9:
             mg.search_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==10:
             mg.sort_tasks(tasks)
             save_tasks(tasks)
             input("\nPress enter to return to menu...")
         elif choice==11:
             break
         


if __name__=="__main__":
    main()
