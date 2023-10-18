import random
print("Welcome to Guessing game where computr Guesses the number\nNow have a number in your mind\n")
num=int(input("enter a number that is greater than the number in your mind"))
guess=''
low=0
high=num
feedback=''

while(feedback!='C'):
    x=random.randint(low,high)
    print(f"Is {x} is the number")
    feedback=input("Enter:\n (L) if guess if Less \n(G) if guess is  Greater \n(C) for correct guess\n:->").upper()
    if(feedback == 'L'):
        low=low+1
    elif(feedback == 'G'):
        high=high-1
    elif (feedback == 'C'):
        print("\nYes I gessed It ;)")
    
    


      


