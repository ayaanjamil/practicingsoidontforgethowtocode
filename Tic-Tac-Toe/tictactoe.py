import random
import time

def displayBoard(board):
    print("\n"*10)
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[1]} | {board[2]} | {board[3]}")

theBoard = ['dummy',' ',' ',' ',' ',' ',' ',' ',' ',' ']
boardwhichisfull = ['#','X','O','X','O','X','O','X','O','X']

def playerInput():
    m = ""
    while not (m == "X" or m == "O"):
        m = input("P1: X or O? - ").upper()
    if m == "X":
        return ("X", "O")
    elif m == "O":
        return("O", "X")

def placeMarker(b, m, p):
    b[p] = m

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return "P1"
    else:
        return "P2"

def spaceFree(b, p):
    return (b[p] == " ")

def boardFull(b):
    for i in range(10):
        if spaceFree(b, i):
            return False
    return True

def choice(b):
    p = 0
    while int(p) not in range(1,10) or not spaceFree(theBoard, int(p)):
        p = input("Position - ")
    return p

def winCheck(b, m):
    return ((b[7] == m and b[8] == m and b[9] == m) or
    (b[4] == m and b[5] == m and b[6] == m) or
    (b[1] == m and b[2] == m and b[3] == m) or
    (b[7] == m and b[4] == m and b[1] == m) or
    (b[8] == m and b[5] == m and b[2] == m) or
    (b[9] == m and b[6] == m and b[3] == m) or
    (b[7] == m and b[5] == m and b[3] == m) or
    (b[9] == m and b[5] == m and b[1] == m))

a = 0
p1m, p2m = playerInput()
t = whoGoesFirst()
print(f"{t} will go first")
time.sleep(1)

while a == 0:
    if t == "P1":
        displayBoard(theBoard)
        p = choice(theBoard)
        placeMarker(theBoard, p1m, int(p))
        if winCheck(theBoard, p1m):
            displayBoard(theBoard)
            print("Congo you won")
            a = 1
        elif boardFull(theBoard):
            print("Draw")
            a = 1
        else:
            t = "P2"
    elif t == "P2":
        displayBoard(theBoard)
        p = choice(theBoard)
        placeMarker(theBoard, p2m, int(p))
        if winCheck(theBoard, p2m):
            displayBoard(theBoard)
            print("Congo you won")
            a = 1
        elif boardFull(theBoard):
            print("Draw")
            a = 1
        else:
            t = "P1"
