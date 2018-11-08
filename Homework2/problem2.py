import random
number = random.randint(1, 100)
guess = 0
tries = 0
while guess != number:
    guess = int( input ("Make a guess: ") )
    if guess == str("exit"):
        break
    tries = tries + 1
     
    if guess == number:
        print("exactly right ")
    elif guess < number:
        print("Too Low ")
    else:
        print("Too high ")
print("Number of tries:", tries)
