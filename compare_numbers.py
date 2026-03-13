from random import randint
def func():
    while True:
        while True:
            print("\n \t\t\t\t===PUT THE SIGN ===\n"
                    "    \t\t\t\t    WORKSHEET   \n ")
            try:
                x=int(input("How many questions do you want: "))
                if x<=0:
                    raise ValueError
                break
            except ValueError:
                print("Enter a numeric value greater than zero")
        
        wrong_ques=[]
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
                wrong_ques.append(i)
                
        print(f"\nScore: {score}/{x}")
        if score==x:
            print("Excellent")
            print("All questions are correct 💯")
        elif len(wrong_ques)==1:
            print(f"Q{wrong_ques[0]} is wrong❌")
        else:
            print(", ".join("Q"+str(i) for i in wrong_ques),end=" ")
            print("are wrong❌")
            
        replay=input("\nReplay (yes/no)?: ").lower().strip()
        if replay!="yes": 
             print("Program ended")
             break 

    
if __name__=="__main__":
    func()
