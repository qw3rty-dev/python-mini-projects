import random

def rps():
        
    result={"rock":"paper","paper":"scissors","scissors":"rock"}
    emoji={"rock":"👊","paper":"🤚","scissors":"✂️"}
    while True:
        choice=input("\nChoose Rock,Paper or Scissors: ").lower().strip()
        if choice in result:
            break
        print("Invalid Input")
        
    computer=random.choice(list(result.keys()))
    print(f"\nYou:{choice.capitalize()}{emoji[choice]}  Computer:{computer.capitalize()}{emoji[computer]}")

    if computer==choice:
        print("It's a draw")
        return 0,0
    
    elif result[computer]==choice:
        print("You won")
        return 1,0
    else:
        print("You lose")
        return 0,1
    
def play_game():
    while True:
        print("\n \t\t\t\t===ROCK PAPER SCISSORS===\n"
            "    \t\t\t\t     (BEST OF THREE)")  
        won=0
        lose=0
        round_no=0
        while won<2 and lose<2:
            w,l=rps()
            won+=w
            lose+=l
            round_no+=1
            print(f"Round {round_no} results >>>  Computer:{lose} | You:{won}")
            
        if won==2:
            print("\n🎊🎊 Congrats,You won 🎊🎊")
        else:
            print("\nYou lose,Try again")
        
        replay=input("\nReplay (yes/no)?: ").lower().strip()
        if replay!="yes": 
             print("Program ended")
             break    
          
        

if __name__=="__main__":
    play_game()



    

     


