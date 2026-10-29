import random

# random number
r=random.randint(1,100)
e=0
guesses=1
# player guess
while(e!=2):
    n=int(input("Guess the number from (1-100):"))
    if r>n:
        guesses+=1
        print("your guess is low")
    elif n>r:
        guesses+=1
        print("your guess is high")
    else:
        print(f"your guess is correct the number is : {r} \nIt took you {guesses} guesses")
        e=2 # a condition to terminate the loop nothing else