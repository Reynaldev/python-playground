from random import randint

num = randint(1, 10)
lim = 0

while lim < 3:
    print("Guess a Number game")
    x = int(input("Input : "))

    if x < num:
        print("To Low!")
        lim += 1
    elif x > num:
        print("To High!")
        lim += 1
    elif x == num:
        print("You Win!")
        break
    elif x > 10:
        print("You just need to answer from 1 to 10")
        break
    else:
        print("Invalid Input!")
        break

if lim == 3:
    print("You Lose!")
    print("The answer is : ", num)
    
