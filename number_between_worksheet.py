import random
def func():
    while True:
        while True:
            print("\n \t\t\t\t===WHAT COMES IN BETWEEN===\n"
                    "    \t\t\t\t         WORKSHEET   \n ")
            try:
                x=int(input("How many questions do you want: "))
                if x<=0:
                    raise ValueError
                break
            except ValueError:
                print("Enter a numeric value greater than zero")

    
        score=0
        wrong_ques=[]
        for i in range(1,x+1):
            n=random.randint(11,100)
            while True:
                    try:
                        print(f"{i}.)   {n} __ {n+2}",end="  ")

                        between=int(input(" ").strip())
                        if between==n+1:
                            score+=1
                        
                        else:
                            wrong_ques.append(i)
                        break
                
                    except ValueError:
                        print("Enter a numeric value")
                        

                
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
