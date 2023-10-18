import random
x=int(input("\n\nEnter the greatest number you want to guess\n->"))
num=random.randint(1,x)
guess=0
while num!=guess:
    guess=int(input("Enter the Guessed number:"))
    if(guess<num):
        print("guessed number is less than the actual number")
    elif(guess>num):
        print("guessed number is greater than the actual number")
    else:
        print("You guessed it Right:)!")
