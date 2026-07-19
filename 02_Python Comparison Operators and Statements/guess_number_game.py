#Guess Number Game


from random import randint
goal_num = randint(1,100)

print("=======================================================")
print("Welcome to Random Number Game, Guess the Number and WIN")
print("=======================================================")

print("RULES:")
print("The Goal is between 1 to 100")
print()

entry = 0
guess_list = []

running = True
while running:
    entry = int(input("Guess the NUMBER: "))

    if entry >100 or entry < 1:
        print("Warning! OUT OF BOUNDS")
    if entry <= 100 and entry >= 1:
        guess_list.append(entry)

        if entry == goal_num:
            print("Good Job, Congratulation. The Goal is:", goal_num)
            print(len(guess_list),"Guesses it took!")
            running = False
            continue

        diffrence = abs(entry - goal_num)
        if len(guess_list) == 1:
            if diffrence <= 10:
                print("WARM!")
            elif diffrence > 10:
                print("COLD!")

        if len(guess_list) >=2:
            prev_guess_dif = abs(guess_list[-2] - goal_num)
            if diffrence < prev_guess_dif:
                print("WARMER!")
            if diffrence > prev_guess_dif:
                print("COLDER!")
