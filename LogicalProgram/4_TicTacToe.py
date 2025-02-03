import numpy as np

def rules(arr):
    global checker
    checker=0
    while True:
        if arr[0][0]==arr[0][1]==arr[0][2]=='X' or arr[0][0]==arr[0][1]==arr[0][2]=='O':
            checker=1
            return True
        elif arr[1][0]==arr[1][1]==arr[1][2]=='X' or arr[1][0]==arr[1][1]==arr[1][2]=='O':
            checker=1
            return True
        elif arr[2][0]==arr[2][1]==arr[2][2]=='X' or arr[2][0]==arr[2][1]==arr[2][2]=='O':
            checker=1
            return True
        elif arr[0][0]==arr[1][0]==arr[2][0]=='X' or arr[0][0]==arr[1][0]==arr[2][0]=='O':
            checker=1
            return True
        elif arr[0][1]==arr[1][1]==arr[2][1]=='X' or arr[0][1]==arr[1][1]==arr[2][1]=='O':
            checker=1
            return True
        elif arr[0][2]==arr[1][2]==arr[2][2]=='X' or arr[0][2]==arr[1][2]==arr[2][2]=='O':
            checker=1
            return True
        elif arr[0][0]==arr[1][1]==arr[2][2]=='X' or arr[0][0]==arr[1][1]==arr[2][2]=='O':
            checker=1
            return True
        elif arr[0][2]==arr[1][1]==arr[2][0]=='X' or arr[0][2]==arr[1][1]==arr[2][0]=='O':
            checker=1
            return True
        else:
            return False           

def play_game(arr):
    print("Player 1: X\nPlayer 2: O")
    for i in range(9):
        if i%2==0:
            print("Player 1's turn")
            row=int(input("Enter row: "))
            col=int(input("Enter column: "))
            arr[row][col]='X'
            print(arr)
            if rules(arr)==True:
                print("Player 1 wins!!")
                break
        else:
            print("Player 2's turn")
            row=int(input("Enter row: "))
            col=int(input("Enter column: "))
            arr[row][col]='O'
            print(arr)
            if rules(arr)==True:
                print("Player 2 wins!!")
                break

arr=np.array([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']])
play_game(arr)
if checker==0:
    print("Match Draw!!")
else:
    pass
