import random

print("Rock Paper Scissors")
def rps():
    d1={"rock":1,"paper":2,"scissors":3}
    rd1={1:"Rock",2:"Paper",3:"Scissors"}
    while True:
        choice=input("Choose Rock,Paper or Scissors: ").lower().strip()
        if choice in d1:
            break
        print("Invalid Input")
            
    user_input= d1[choice]
    computer=random.randint(1,3)

    print(f"You:{rd1[user_input]}  Computer:{rd1[computer]}")
    



    if computer==user_input:
        print("It's a draw")
        return 0,0
    elif (user_input == 1 and computer == 3) or \
     (user_input == 2 and computer == 1) or \
     (user_input == 3 and computer == 2):
        print("You won")
        return 1,0
    else:
        print("You lose")
        return 0,1
def play_game():
    print("Best of three")
    won=0
    lose=0
    round_no=0
    while won<2 and lose<2:
        w,l=rps()
        won+=w
        lose+=l
        round_no+=1
        print(f"Round {round_no} results >>> Computer:{lose}  You:{won}")
        

    if won==2:
        print("Congrats you won")
    else:
        print("You lose,Try again")

if __name__=="__main__":
    play_game()



    

     


