import random

def zahras_rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    
    users_choice = input("enter your choice ( rock, paper, or scissors): ").lower().strip()

    while users_choice not in choices:
        print("incorrect choice entered. please retry.")
        users_choice = input("enter your choice (rock, paper, or scissors): ").lower().strip()



    computers_choice = random.choice(choices)

    print(f"\nYou picked: {users_choice}")
    print(f"Computer picked: {computers_choice}")


    if users_choice == computers_choice:
        print( "it is a draw!")
    elif (users_choice == "paper" and computers_choice == "rock") or \
         (users_choice == "rock" and computers_choice == "scissors") or \
         (users_choice == "scissors" and computers_choice == "paper"):
        print("You are the winner!")
    else:
        print("Computer is the winner!")

if __name__ == "__main__":
    while True:
        zahras_rock_paper_scissors()
        again = input("Type 'stop' to quit or press Enter to play again: ").lower().strip()
        if again == "stop":
            print("Thanks for playing. Goodbye!")
            break


    
