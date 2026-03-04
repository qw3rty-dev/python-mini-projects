from random import randint
def hint(num,guess):
        

    if(num==guess):
        print(f"Congrats,You guessed it right,it was {num}")
        return True
    diff=abs(num-guess)
    if(diff<=2):
        print("Very close")
    elif( diff<=5):
        print("Close")
    else:
        print("Try again")
    return False
def play_game():
    while True:
        print("Number Guessing game ")
        print("You will be given 3 chances to guess the number ranging between 1 to 20")

        num=random.randint(1,20)
        for i in range(3):
            while True:
                try:
                    guess=int(input(f"Guess {i+1}: "))
                    if guess in range(1,20):
                        break
                    else:
                        print("Enter a number from 1 to 20")
                except ValueError:
                    print("Enter an integer")

            
            if hint(num,guess):
                break
        else:
            print("Sorry,you have used all ur guesses")

        print(f"The number was {num}")
        print("Do you wish to replay >> Yes or no(enter any random str): ",end="")
        z=input()
        if z.lower().strip()!="yes":
            break


if __name__=="__main__":
    play_game()
