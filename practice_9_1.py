import random

x=random()
print(x)
dice1=random.randint(1,6)
dice2=random.randint(1,6)

print("dice1:", dice1,"dice2:",dice2)

if (dice1==dice2):
    print("You are a winner")
else:
    print("You lose")