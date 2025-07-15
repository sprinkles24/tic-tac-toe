import random # This code was made freely available at https://docs.python.org/3/library/random.html
import os # This code was made freely available at https://docs.python.org/3/library/os.html

Av, Bv, Cv, Dv, Ev, Fv, Gv, Hv, Iv = " ", " ", " ", " ", " ", " ", " ", " ", " "
playerChoiceG = ""


staticBoard = """Key:\n\n
            .      .
        A   .  B   .   C  
            .      .      
       . . . . . . . . . . 
            .      .
        D   .  E   .   F  
       . . . . . . . . . . 
            .      .
        G   .  H   .   I   
            .      .\n\n"""


stringBoard = ("""\n
            .      .
         {A}  .  {B}   .   {C}  
            .      .      
       . . . . . . . . . . 
            .      .
         {D}  .   {E}  .   {F}  
       . . . . . . . . . . 
            .      .
         {G}  .   {H}  .   {I}   
            .      .""")

legalMovesList = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
winList = [[lambda:Av, lambda:Bv, lambda:Cv], [lambda:Dv, lambda:Ev, lambda:Fv], [lambda:Gv, lambda:Hv, lambda:Iv], [lambda:Av, lambda:Dv, lambda:Gv], [lambda:Bv, lambda:Ev, lambda:Hv], [lambda:Cv, lambda:Fv, lambda:Iv], [lambda:Av, lambda:Ev, lambda:Iv], [lambda:Cv, lambda:Ev, lambda:Gv]]


def inputPosition(playerChoice):
    global box
    randLegalMove = random.choice(legalMovesList)
    while box not in legalMovesList:
        print(f"It's {playerChoice} 's turn!\n")
        box = (input(f"Type a letter that corresponds to an empty spot on the grid. For example, {randLegalMove}.")).upper()
    
    global Av, Bv, Cv, Dv, Ev, Fv, Gv, Hv, Iv
    
    
    
    if box == "A":
        Av = playerChoice
    elif box == "B":
        Bv = playerChoice
    elif box == "C":
        Cv = playerChoice
    elif box == "D":
        Dv = playerChoice
    elif box == "E":
        Ev = playerChoice
    elif box == "F":
        Fv = playerChoice
    elif box == "G":
        Gv = playerChoice
    elif box == "H":
        Hv = playerChoice
    elif box == "I":
        Iv = playerChoice
    
    legalMovesList.remove(box)
    os.system("clear")
    print(staticBoard)
    print(stringBoard.format(A = Av, B = Bv, C = Cv, D = Dv, E = Ev, F = Fv, G = Gv, H = Hv, I = Iv))
    
def checking_winList(playerChoice):
    global gameOver
    for eachList in winList:
        posValue = [position() for position in eachList]
        if posValue[0] == posValue[1] == posValue[2] and posValue[0] != " ":
            os.system("clear")
            print(stringBoard.format(A = Av, B = Bv, C = Cv, D = Dv, E = Ev, F = Fv, G = Gv, H = Hv, I = Iv))
            print(f"{playerChoice} wins!")
            gameOver = True
            return
    if len(legalMovesList) == 0:
        print("Draw!")
        gameOver = True
        return


print("Welcome to Tic-Tac-Toe!\n\nThis is a 2-player game.\n\n")
playerChoiceG = input("Would Player 1 like to play as X or O? ")

while playerChoiceG.lower() not in ["x", "o", "O", "0"]:
    playerChoiceG = input("Type X or O. ")


if playerChoiceG.lower() == "x":
    playerChoiceG = playerChoiceG.lower()
    print("Player 2 will play as ◯ .")
else:
    playerChoiceG = "◯"
    print("Player 2 will play as X.")

print("\n\n" + staticBoard)

box = None

gameOver = False

while gameOver == False:
    if len(legalMovesList) == 9:
      playerChoiceG = random.choice(["x", "◯"])
    elif playerChoiceG == "x":
        playerChoiceG = "◯"
    elif playerChoiceG == "◯":
        playerChoiceG = "x"
    
    inputPosition(playerChoiceG)
    checking_winList(playerChoiceG)

print("\n\nThanks for playing!")


