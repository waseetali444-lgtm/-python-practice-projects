print("ROCK PAPER SCISSORS GAME")
print("select your choice:")
print("1. Rock ✊ ")
print("2. Paper ✋")
print("3. Scissors✌️")
print("4. lizard 🦎")
print("5. Spock 🖖")
print("enter your choice(1-5):")
player_choice = int(input("enter your choice(1-5):"))
import random
cpu_choice = random.randint(1, 5)
print("CPU choice:", cpu_choice)
if player_choice == cpu_choice:
    print("It's a tie!")
elif (player_choice == 1 and (cpu_choice == 3 or cpu_choice == 4)) or \
     (player_choice == 2 and (cpu_choice == 1 or cpu_choice == 5)) or \
     (player_choice == 3 and (cpu_choice == 2 or cpu_choice == 4)) or \
     (player_choice == 4 and (cpu_choice == 2 or cpu_choice == 5)) or \
     (player_choice == 5 and (cpu_choice == 1 or cpu_choice == 3)):
    print("You win!")
else:
    print("You lose!")