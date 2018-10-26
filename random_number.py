#First lesson:
import random

running = True

while running:
    max_number = int(input("Choose the maximum number: "))
    correct_answer = random.randint(0,max_number)
    correct = False
    while not correct:
        guess = int(input("Guess:"))
        if guess == correct_answer:
            print ("You've won!!!")
            correct = True
        elif guess > correct_answer:
            print ("Too high!")
        elif guess < correct_answer:
            print ("Too low!")
