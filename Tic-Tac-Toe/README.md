# Tic-Tac-Toe

Does what it says.

Very simple tic-tac-toe game made in Python.

### Functions

```py
def displayBoard(board):
    print("\n"*10)
    print(f"{board[7]} | {board[8]} | {board[9]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[1]} | {board[2]} | {board[3]}")
```

Prints out the board

```py
def playerInput():
    m = ""
    while not (m == "X" or m == "O"):
        m = input("P1: X or O? - ").upper()
    if m == "X":
        return ("X", "O")
    elif m == "O":
        return("O", "X")
```

Allots player sides

```py
def whoGoesFirst():
    if random.randint(0,1) == 0:
        return "P1"
    else:
        return "P2"
```

Decides who goes first

```py
def spaceFree(b, p):
    return (b[p] == " ")
```

Checks whether the space is free in the board or not

```py
def boardFull(b):
    for i in range(10):
        if spaceFree(b, i):
            return False
    return True
```

Checks whether the board is full or not

```py
def choice(b):
    p = 0
    while int(p) not in range(1,10) or not spaceFree(theBoard, int(p)):
        p = input("Position - ")
    return p
```

Inputs choice from user

```py
def winCheck(b, m):
    return ((b[7] == m and b[8] == m and b[9] == m) or
    (b[4] == m and b[5] == m and b[6] == m) or
    (b[1] == m and b[2] == m and b[3] == m) or
    (b[7] == m and b[4] == m and b[1] == m) or
    (b[8] == m and b[5] == m and b[2] == m) or
    (b[9] == m and b[6] == m and b[3] == m) or
    (b[7] == m and b[5] == m and b[3] == m) or
    (b[9] == m and b[5] == m and b[1] == m))
```

Checks for wins
