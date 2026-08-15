
import random

symbols = ['🍒', '🍇', '🍉', '7️⃣']
results = random.choices(symbols, k=3)

for i in range(len(results)):
    if i == len(results) - 1:
        print(results[i])
    else:
        print(results[i], end=" | ")
if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
    print("You have won!")
else:
    print("You have lost!")