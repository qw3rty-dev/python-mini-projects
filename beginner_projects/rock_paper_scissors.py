import random
import os 

def rps(round_no):
    
    result={"rock":"paper","paper":"scissors","scissors":"rock"}
    emoji={"rock":"👊","paper":"🤚","scissors":"✂️"}
    while True:
        choice=input("\nChoose Rock,Paper or Scissors: ").lower().strip()
        if choice in result:
            break
        print("Invalid Input")
        
    
    computer=random.choice(list(result.keys()))

    print(f"\n--- Round {round_no} ---\n")
    print(f"You:{choice.capitalize()}{emoji[choice]}")
    print(f"Computer:{computer.capitalize()}{emoji[computer]}\n")
    

    if computer==choice:
        print("Result: It's a draw")
        return 0,0
    
    elif result[computer]==choice:
        print("Result: You won")
        return 1,0
    else:
        print("Result: You lose")
        return 0,1
    
def clear():
    os.system("cls" if os.name=="nt" else "clear")


def play_game():
    while True:
        clear()
        print("\n\n"+"="*30)
        print("ROCK PAPER SCISSORS".center(30))
        print("(BEST OF THREE)".center(30))
        print("="*30)

        won=0
        lose=0
        round_no=1
        while won<2 and lose<2:
            w,l=rps(round_no)
            won+=w
            lose+=l
            round_no+=1
            print("\nScore: ")
            print(f"You       : {won}")
            print(f"Computer  : {lose}")
            print("-"*30)

            
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



    

     


