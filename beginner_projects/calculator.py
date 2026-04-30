import os


def add(a,b):
    result= a+b
    return int(result) if int(result)==result else result
    
def sub(a,b):
    result= a-b
    return int(result) if int(result)==result else result


def div(a,b):
    result= a/b
    return int(result) if int(result)==result else result

def mul(a,b):
    result= a*b
    return int(result) if int(result)==result else result

def fact(n):
    if(n==0 or n==1):
        return 1
    elif n<0:
         raise ValueError("Factorial not defined for -ve numbers")
    else:
        return n*fact(n-1)
    

def menu():
    print("\n\n"+"="*40)
    print("CALCULATOR".center(40))
    print("="*40)
    print(
          f"[+] for ADDITION\n"
          "[-] for SUBTRACTION\n"
          "[*] for MULTIPLICATION\n"
          "[/] for DIVISION\n"
          "[f] for FACTORIAL\n"
          "[exit] to EXIT\n"
          )
    oplist=["+",'-','*','/',"f","exit"]
    while True:
        operation=input("CHOOSE: ").strip().lower()
        if operation not in oplist :
            print("INVALID OPERATION")
            continue
        return operation
    
    
def input_number(msg):
    while True:
        try:
             return float(input(msg))
        except ValueError:
             print("Invalid number try again")
def input_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Enter a valid integer")

def input_values():
        a= input_number("Enter 1st number: ")
        b= input_number("Enter 2nd number: ")
        return a,b
    
def clear():
     os.system("cls" if os.name=="nt" else "clear")

def pause():
    input("\nPress enter to return to menu")

    
def calculator():
    while True:
        clear()
        operation=menu()

        if operation=="exit":
            print("Program ended")
            break
           
        if operation.lower()=="f":
            try:
                a= input_int("ENTER THE NUMBER: ")
                print(fact(a))
                pause()
                        
            except ValueError as e:
                    print(e)
                    pause()
            continue
                    
        a,b= input_values()
        if operation== "+":
            print(add(a,b))
            pause()
        elif operation== "-":
            print(sub(a,b))
            pause()
        elif operation== "*":
            print(mul(a,b))
            pause()
        elif operation== "/":
            try:
                print(div(a,b))
                pause()
            except ZeroDivisionError:
                print("Can't Divide by zero")    
                pause()
                
            

if __name__=="__main__":
     calculator()
    
