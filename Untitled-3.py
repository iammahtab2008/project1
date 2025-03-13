import random

random_num = random.randint(1, 99)

print("Guess a number between 1 and 99. You have 5 chances!")


for i in range(5):
    guess = int(input('guess a number= '))
    
    if guess < random_num:
        print("The number is bigger!")
    elif guess > random_num:
        print("The number is smaller!")
    else:
        print("Congratulations! You guessed the number correctly!")
        break
else:
    print(f"Out of chances! The number you were looking for was {random_num}.")