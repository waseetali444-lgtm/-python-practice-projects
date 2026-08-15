
import random

winning_numbers = []
while len(winning_numbers) < 5:
    num = random.randint(1, 26)
    if num not in winning_numbers:  # avoid duplicates
        winning_numbers.append(num)

print("Winning numbers:", winning_numbers)

player_numbers = []
print("Pick 5 numbers between 1 and 26:")
while len(player_numbers) < 5:
    num = int(input("Enter a number: "))
    if num not in player_numbers:
        player_numbers.append(num)
matches = 0
for number in player_numbers:
    if number in winning_numbers:
        matches += 1

print("You matched", matches, "numbers!")

if matches == 5:
    print("JACKPOT! You won everything!")
elif matches >= 3:
    print("Nice, you won a small prize!")
else:
    print("Sorry, better luck next time.")