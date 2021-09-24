import random

tomb = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
game = 1

def display_game():
    print(tomb[0] + ' | ' + tomb[1] + ' | ' + tomb[2])
    print('-   -   -')
    print(tomb[3] + ' | ' + tomb[4] + ' | ' + tomb[5])
    print('-   -   -')
    print(tomb[6] + ' | ' + tomb[7] + ' | ' + tomb[8])

def player_turn():
    hova = " "
    hova = input("Hova teszed az 'X'-et? Írj be számot (1-9)")
    hova = int(hova)
    if hova < 1 or hova > 9:
        print("Nem megfelelő számot adott meg")
        player_turn()
    else:
        if tomb[hova-1] == " ":
            tomb[hova-1] = "X"

        else:
            print("Ezen a helyen már van szimbólum")
            player_turn()

def game_check():
    global game
    all = 0
    for i in tomb:
        if i != " ":
            all+=1

    if all == 9:
        game = 0

    if tomb[0] == tomb[1] == tomb[2] and tomb[0] != " ":
       game = 0
    if tomb[3] == tomb[4] == tomb[5] and tomb[3] != " ":
       game = 0
    if tomb[6] == tomb[7] == tomb[8] and tomb[6] != " ":
       game = 0

    if tomb[0] == tomb[3] == tomb[6] and tomb[0] != " ":
       game = 0
    if tomb[1] == tomb[4] == tomb[7] and tomb[1] != " ":
       game = 0
    if tomb[2] == tomb[5] == tomb[8] and tomb[2] != " ":
       game = 0

    if tomb[0] == tomb[4] == tomb[8] and tomb[0] != " ":
       game = 0
    if tomb[2] == tomb[4] == tomb[6] and tomb[2] != " ":
       game = 0

def ai_turn():
    move = random.randint(0 , 8)
    if tomb[move] == " " :
        tomb[move] = "O"
    else:
        ai_turn()

while game == 1:
    display_game()
    player_turn()
    game_check()
    if game == 1:
        ai_turn()
    else:
        break
    game_check()

display_game()
print("GAME OVER")