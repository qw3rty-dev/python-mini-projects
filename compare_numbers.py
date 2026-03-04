from random import randint
def func():
    while True:
       try:
           x=int(input("How many questions do you want: "))
           if x<=0:
               raise ValueError
           break
       except ValueError:
           print("Enter a numeric value greater than zero")
    print("===Worksheet=== \nPut the sign ")
   
    l2=[]
    signs=["=","<",">"]
    score=0
    for i in range(1,x+1):
        num= randint(10,100)
        num2=randint(10,100)
        

        while True:
            print(f"{i}.) {num} __ {num2}",end=" ")
            sign=input( ).strip()
            
            if sign not in signs:
                print("Enter a Valid sign")
                continue
            break
        if ((num>num2 and sign == ">") or
              (num<num2 and sign=="<") or
              (num==num2 and sign=="=")):
            score+=1
            
        else:
            l2.append(i)
            
            

    print(f"Score: {score}/{x}")
    if score==x:
        print("Excellent")
        print("All questions are correct")
    elif len(l2)==1:
        print(f"Q{l2[0]} is wrong")
    else:
        print(", ".join("Q"+str(i) for i in l2),end=" ")
        print("are wrong")
    


if __name__=="__main__":
    func()
