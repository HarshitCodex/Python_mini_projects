import random
print("Welcome people. I am Harshit trying to learn python . Lets play a game to generate random number ")
r = random.randint(1, 100)
print("Guess the number I have generated randomly from 1-100 inclusive ")
u = input("Enter your guess ")
u = int(u)
if r == u:
    print("The answer is right : " + str(r))
else:
    print("Oops! The correct answer is : " + str(r))
