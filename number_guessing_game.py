from random import randint

def guessGame():
    while True:
        print("\t\t\t\t\t===GUESSING GAME===\n" 
        "\t\t\t\t Guess the number ranging between 1 to 20\n"
        "\t\t\t\t           You have 3 chances")
        num=randint(1,20)
        print(num)
        for i in range(1,4):
            while True:
                 try:
                    guess=int(input(f"Guess {i}: "))
                    if guess in range(1,21):
                         break
                    else:
                         print("Enter a number ranging between 1 to 20")
                         
                 except ValueError:
                    print("Invalid input")
            if logic(num,guess):
                break
        else:
            print("\nYou have used all your guesses")
        print(f"The number was {num}")
        
        re = input("\nReplay? (yes/no): ").lower().strip()
        if re!="yes":
            print("\nProgram ended")
            break

      
def logic(num,guess):
    if num==guess:
        print(f"\n🎊🎊 Congrats,You guessed it right 🎊🎊")
        return True
    if abs(num-guess)<=3:
        print("Very close")
    elif abs(num-guess)<=5:
        print("Close")
    else:
        print("Not even close")
    return False

    


if __name__=="__main__":
    guessGame()
