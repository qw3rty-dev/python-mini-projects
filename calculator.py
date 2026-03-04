def add(a,b):
    return a+b
    

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def mul(a,b):
    return a*b

def fact(n):
    if(n==0 or n==1):
        return 1
    elif n<0:
         raise ValueError("Factorial not defined for -ve numbers")
    else:
        return n*fact(n-1)
    

def menu():
    print("""
          Type:
          + for ADDITION
          - for SUBTRACTION
          * for MULTIPLICATION
          / for DIVISION
          f for FACTORIAL
          . to STOP""")
    
def input_number(msg):
    while True:
        try:
             return float(input(msg) )
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
    
    
def calculator():
    oplist=["+",'-','*','/','.',"f","F"]
    
    while True:
        menu()
        operation=input("CHOOSE: ").strip()
        if operation not in oplist :
            print("INVALID OPERATION")
            continue

        if operation==".":
            print("Program ended")
            break
           
        if operation.lower()=="f":
                
                    try:
                        a= input_int("ENTER THE NUMBER: ")
                        print(fact(a))
                        
                    except ValueError as e:
                        print(e)
                    continue
        a,b= input_values()
        if operation== "+":
               print(add(a,b))
        elif operation== "-":
               print(sub(a,b))
        elif operation== "*":
               print(mul(a,b))
        elif operation== "/":
               try:
                print(div(a,b))
               except ZeroDivisionError:
                    print("Can't Divide by zero")    
            

if __name__=="__main__":
     calculator()
    
