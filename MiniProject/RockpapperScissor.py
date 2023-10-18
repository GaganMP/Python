import random
str=input("Ready to play Rock paperScissor Y/N")

win={("R","P"):"P",("R","S"):'R',("P","R"):"P",("P","S"):"S",("S","R"):'R',("S","P"):"S"}


while( str=="Y"):
    print("computer making its choice\n")
    compch=random.choice(['R',"P","S"])
   
    Userch=input("Enter your choice")
    print(f"{compch} vs {Userch}")
    if(compch==Userch):
        print("Draw")
    elif(win[(compch,Userch)]==compch):
        print("computer wins")
    elif(win[(compch,Userch)]==Userch):
        print("Player wins the game")

    str=input("Do you want to play press Y/N")

