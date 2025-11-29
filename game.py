import random

print("Welcome to Rock-Paper-Scissors Game")
print("1.rock")
print("2.paper")
print("3.scissors")

options = ["1","2","3","4"]
new=["1.rock","2.paper","3.scissors"]
while True:
    user_choice = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user_choice in ['1','2','3','4']:
     if user_choice == "4":
        print("Thanks for playing! Goodbye!")
        break

    if user_choice not in options:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose:{computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "1" and computer_choice == "3") or \
         (user_choice == "2" and computer_choice == "1") or \
         (user_choice == "3" and computer_choice == "2"):
       print("You win!")
    else:
        print("You lose!")
