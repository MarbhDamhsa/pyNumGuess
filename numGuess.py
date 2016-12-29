import random

number = random.randrange(1,501)
guessLimit = 10
guessCount = 1
done = False

print("I'm thinking of a number between 1 and 500")

while not done:
    while guessCount <= guessLimit:
        print("--- Guess # ", guessCount)
        guess = int(input("Your guess: "))
        if (guess < number):
                    print("Too low!")
                    guessCount += 1
        elif (guess > number):
                    print("Too high!")
                    guessCount += 1                
        elif (guess == number):
                    print("Congratulations!")
                    guessCount += guessLimit
                    done = True
        if (guessCount > guessLimit) and done == False:
            print("GAME OVER! The number was ", number)
            done = True
