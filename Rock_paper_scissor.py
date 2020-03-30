import random


def chs(r):
    if r == 1:
        return "Rock"
    elif r == 2:
        return "Paper"
    else:
        return "Scissor"


y = 1
while y == 1:
    use = int(input("Choose Number" + "\n" + "1.Rock 2.Paper 3.Scissor "))
    r = random.randint(1, 3)
    if use not in [1, 2, 3]:
        print("Invalid. I am angry. Bye")
        break
    print("You have chosen " + chs(use))
    print("Computer chooses " + chs(r))
    if use == r:
        print("Its a draw.")
    elif use == 1:
        if r == 2:
            print("Computer wins")
        else:
            print("You win")
    elif use == 2:
        if r == 3:
            print("Computer wins")
        else:
            print("You win")
    elif use == 3:
        if r == 1:
            print("Computer wins")
        else:
            print("You win")
    y = int(input("Enter 1 to continue playing the game "))
