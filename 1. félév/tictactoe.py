import random

while True:        
    board = [
        [" ", "1", "2", "3"],
        ["1", "-", "-", "-"],
        ["2", "-", "-", "-"],
        ["3", "-", "-", "-"]
    ]

    def show_board():
        for i in range(len(board)): # i = 0, 1, 2, 3
            print(board[i][0], board[i][1], board[i][2], board[i][3])
    computer_opponent = True
    mode = input("Milyen módban szeretnél játszani? (1 - számítógép ellen, 2 - két játékos)\n")
    if mode == "2":
        computer_opponent = False
    player_1_turn = True
    have_winner = False
    while not have_winner:
        # Jelenítsük meg a játék aktuális állását
        show_board()

        # Írjuk ki, hogy melyik játékos következik
        if player_1_turn:
            print("Az első játékos következik.")
        else:
            print("A második játékos következik.")

        # Olvassuk be, hogy hova lép az aktív játékos
        correct_placement = False
        while not correct_placement:
            row = 10
            col = 10
            if player_1_turn or not computer_opponent:
                while row < 1 or row > 3:
                    row = int(input("Add meg a kívánt sor sorszámát!\n"))
                while col < 1 or col > 3:
                    col = int(input("Add meg a kívánt oszlop sorszámát!\n"))
            else:
                row = random.randint(1, 3)
                col = random.randint(1, 3)
            if board[row][col] == "-":
                correct_placement = True
                # Erre a pozícióra rakjuk le a játékos jelét (X vagy O)
                if player_1_turn:
                    board[row][col] = "X"
                else:
                    board[row][col] = "O"
        # Ellenőrizzük le, hogy megnyerte-e valaki a játékot
        # Sorok ellenőrzése:
        for i in range(1, len(board)):
            if board[i][3] == board[i][1] and board[i][1] == board[i][2] and board[i][2] != "-":
                have_winner = True
        # Oszlopok ellenőrzése:
        for i in range(1, len(board)):
            if board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[2][i] != "-":
                have_winner = True
        # Átlók ellenőrzése:
        if board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[2][2] != "-":
            have_winner = True
        if board[3][1] == board[2][2] and board[2][2] == board[1][3] and board[2][2] != "-":
            have_winner = True

        # Ellenőrizzük le, hogy betelt-e a tábla, ha igen -> Döntetlen
        if ("-" not in board[1]) and ("-" not in board[2]) and ("-" not in board[3]):
            break
        # Állítsuk át a player_1_trun véltozó értékét az ellentettjére
        if not have_winner:
            player_1_turn = not player_1_turn

    show_board()
    if have_winner:
        if player_1_turn:
            print("X nyert!")
        else:
            print("O nyert!")
    else:
        print("Döntetlen!")
    
    restart = input("Szeretnél újra játszani? (igen/nem)\n")
    if restart != "igen":
        break