import sys
sep="|   |"
board=[[' ']*3 for i in range(3)]
empty=list(range(0,9))
#print(empty)


#print([board[i][j] for i in range(3) for j in range(3) if i+j==2])

def display(board):
    for i in board:
        print(f"|{(sep).join(i) }|\n")
def check(board,row,col):
    if board[row]==['X',"X","X"] or  [board[i][col] for i in range(3)]==['X',"X","X"] or [board[i][i] for i in range(3)]==['X',"X","X"] or [board[i][j] for i in range(3) for j in range(3) if i+j==2]==['X',"X","X"]:
        return (0,'X')
    elif board[row]==['O',"O","O"] or  [board[i][col] for i in range(3)]==['O',"O","O"] or [board[i][i] for i in range(3)]==['X',"X","X"] or [board[i][j] for i in range(3) for j in range(3) if i+j==2]==['O',"O","O"]:
        return (1,'O')
    else:return (-1,' ')
    
    
    
def posToIndex(pos):
    return (pos//3,pos%3)
def userInp(board):
    count=0;
    
    winner=' '
    p1=input("Enter  player1 name\n>>")
    p2=input("Enter player2 name\n>>")
    playname=[p1,p2]
    players=["X","O"]
    while(winner==' '):
        print(f"{playname[count%2]} turn!:")
        
        try:
           inp=int(input("Enter the cell position \n>>"))
        except(ValueError):
            inp=int(input(f"cell position must be of  {empty}\n>>"))
        while(inp not in empty):
            inp=int(input(f"Enter the position among {empty} \n>>"))
        empty.remove(inp)
        indx=posToIndex(inp)
        board[indx[0]][indx[1]]=players[count%2]
        count+=1
        display(board)
        ch,winner=check(board,indx[0],indx[1])
        if(len(empty)==0):
            print("The Match Draw")
            winner="No one won the game"
            quit()
    print(f"{playname[ch]} won the Game\n")
        
        
userInp(board)
input("Enter any key to exit")
