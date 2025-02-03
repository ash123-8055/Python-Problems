import random

flipping_time=int(input("Enter the number of times you want to flip the coin: "))
no_of_heads=0
no_of_tails=0
percentage_of_heads=0
percentage_of_tails=0

if random.random() < 0.5:
    no_of_tails+=1
else:
    no_of_heads+=1

percentage_of_heads=(no_of_heads/flipping_time)*100
percentage_of_tails=(no_of_tails/flipping_time)*100

print(f"The Percentage of Heads flipping for {flipping_time} times is: {percentage_of_heads}")
print(f"The Percentage of Tails flipping for {flipping_time} times is: {percentage_of_tails}")