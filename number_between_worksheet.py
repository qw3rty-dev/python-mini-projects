import random
def func():
    while True:
       try:
           x=int(input("How many questions do you want: "))
           if x<=0:
               raise ValueError
           break
       except ValueError:
           print("Enter a numeric value greater than zero")

    print("===Worksheet=== \n What comes in between ")
    score=0
    l2=[]
    for i in range(1,x+1):
        n=random.randint(11,100)
        while True:
                try:
                    print(f"{i}.) {n} __ {n+2}",end=" ")

                    between=int(input(" ").strip())
                    if between==n+1:
                        score+=1
                    
                    else:
                        l2.append(i)
                    break
             
                except ValueError:
                    print("Enter a numeric value")
                    

            
    print(f"Score: {score}/{x}")
    if score==x:
        print("Excellent")
    else:
        if len(l2)==1:
            print(f"Q{l2[0]} is wrong")
        else:
    
            print(", ".join("Q"+ str(i) for i in l2),end=" ")
            print("are wrong")
            

if __name__=="__main__":
    func()
