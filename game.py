import random
numbers = random.randint(1, 100)
numberofgusses = 0
userguess = None

while (userguess != numbers):
    userguess = int(input("guess the random number"))
    if (userguess == numbers):
        print(" congratulations, you guesse it right ")
        print("number of guesse " + str(numberofgusses))
    elif (userguess > numbers):
        print("sorry, you guessed wrong, the actual number is smaller")
        numberofgusses = numberofgusses + 1
        print("number of guesse " + str(numberofgusses))
    else:
        print("Sorry, you guessed wrong, the actual number is bigger")
        numberofgusses = numberofgusses + 1
        print("number of guesse " + str(numberofgusses))
