#Connect 4 with advance features
class Connect_game:
    def __init__(self):
        global col1
        global row2
        global mul
        col1 = 7
        row1 = 6
        mul = col1 * row1
        self.alpha1 = ["A","B","C","D","E","F","G","H","I","J","K"]
        self.numberOfColumns =col1
        self.numberOfLines = row1
        self.board = [ [ '  ' for _ in range( self.numberOfColumns)] for _ in range(self.numberOfLines) ]
    #Display board
    def display(self):
        print("******************************************************")
        print('   '.join(self.alpha1[x] for x in range(self.numberOfColumns)))
        for i, line in enumerate(self.board):
            print("_" * self.numberOfColumns * 4)
            print(*line, sep=' |')
        print('   '.join(str(x) for x in range(self.numberOfColumns)))
        print("******************************************************")
    #Check Availaible_space
    def availaible_space(self, line, column):
        if line[column] == '  ':
            return True
        return False
    #ask choice which column to enter
    def choice1(self):
        while True:
            try:
                choice = int(input(f"              {currentPlayer} Turn\nPlease select an empty space between 0 and {col1-1} : "))
                # while choice>(col1-1):
                #     choice = int(input(f"Wrong Input!\n{currentPlayer} Please select an empty space between 0 and {col1-1} : "))
                if choice<=(col1-1):
                    break
                else:
                    print("              Wrong Input!")
                    continue
            except:
                print("              Wrong Input!")
                continue
        

        while self.board[0][choice] != '  ':
            choice = int(input(f"This column is full! Please choose between 0 and {col1-1} : "))
        return choice
    #ask input information to start the game
    def input1(self):
        global r_players 
        while True:  
            r_players = input("Enter No of players to Play this game 2 or 3: ")
            if r_players =="2":
                player1 = input("Please pick a marker for Player 1 'X' or 'O' : ")
                print("--------------------------------------------------------")
                while True:
                    if player1.upper() == 'X':
                        print("--------------------------------------------------------")
                        player2='O'
                        print("You've choosen " + player1 + ". Player 2 will be " + player2)
                        return player1.upper(),player2.upper()
                    elif player1.upper() == 'O':
                        print("--------------------------------------------------------")
                        player2='X'
                        print("You've choosen " + player1 + ". Player 2 will be " + player2)
                        return player1.upper(),player2.upper()
                    else:
                        player1 = input("        Wrong Input!\nPlease pick a marker for Player 1 'X' or 'O' : ")
            elif r_players=="3":
                player1 = input("Please pick a marker for Player 1 'X' or 'O' or 'V': ")
                print("--------------------------------------------------------")
                while True:
                    if player1.upper() == 'X':
                        player2 = input("Please pick a marker for Player 2 'v' or 'O': ")
                        print("--------------------------------------------------------")
                        if player2.upper() == 'V':
                            player3='O'
                            print("You've choosen " + player1 + ". Player 2 will be " + player2+ ". Player 3 will be " + player3)
                            return player1.upper(),player2.upper(),player3
                        else:
                            player2='O'
                            player3="V"
                            print("You've choosen " + player1 + ". Player 2 will be " + player2+ ". Player 3 will be " + player3)
                            return player1.upper(),player2.upper(),player3
                    elif player1.upper() == 'O':
                        player2 = input("Please pick a marker for Player 2 'X' or 'V': ")
                        print("--------------------------------------------------------")
                        if player2.upper() == 'V':
                            player3='X'
                            print("You've choosen " + player1 + ". Player 2 will be " + player2+ ". Player 3 will be " + player3)
                            return player1.upper(),player2.upper(),player3
                        else:
                            player2='X'
                            player3="V"
                            print("You've choosen " + player1 + ". Player 2 will be " + player2+ ". Player 3 will be " + player3)
                            return player1.upper(),player2.upper(),player3
                    elif player1.upper() == 'V':
                        player2 = input("Please pick a marker for Player 2 'X' or 'O': ")
                        print("--------------------------------------------------------")
                        if player2.upper() == 'X':
                            player3='O'
                            print("You've choosen " + player1 + ". Player 2 will be " + player2+ ". Player 3 will be " + player3)
                            return player1.upper(),player2.upper(),player3
                        else:
                            player2='O'
                            player3="X"
                            print("You've choosen " + player1 + ". Player 2 will be " + player2+ ". Player 3 will be " + player3)
                            return player1.upper(),player2.upper(),player3
                    else:
                        player1 = input("        Wrong Input!\nPlease pick a marker 'X' or 'O' or 'V': ")
            else:
                r_players = input("        Wrong Input!\nEnter No of players to Play this game 2 or 3: ")
                if r_players == "2" or r_players == "3":
                    continue
                else:
                    print("        Wrong Input!")
    #Check rows fill or not
    def check_rows(self, marker, board=None):
        if board is None:
            board=self.board
        for line in board:
            for i in range(0,len(line)):
                if i < len(line) - 3:
                    if line[i] == line[i+1] == line[i+2] == line[i+3] == " " + marker:
                        return True
    #check columns or diagonals
    def check_cols(self, marker):
        diagBoard = []
        for i, line in enumerate(self.board):
            for idx, item in enumerate(line):
                if item == ' ' + marker:
                    diagBoard.append(int(str(i)+str(idx)))

        for item in diagBoard:
            if int(item) + 11 in diagBoard and int(item) + 22 in diagBoard and int(item) + 33 in diagBoard:
                return True

        for item in reversed(diagBoard):
            if int(item) - 9 in diagBoard and int(item) - 18 in diagBoard and int(item) - 27 in diagBoard:
                return True
    #reversed the board
    def board1(self):
        reversedBoard = []
        for line in self.board:
            for index, item in enumerate(line):
                try:
                    reversedBoard[index].append(item)
                except:
                    reversedBoard.append([])
                    reversedBoard[index].append(item)
        return reversedBoard
    #Place marker on board through  the position given by user
    def play(self, playercolumn, marker):
        for item in reversed(self.board):
            if self.availaible_space(item, playercolumn):
                item[playercolumn] = " " + marker
                return True
        return False

c = Connect_game()

game = True
#While game is true will not end or while game is draw
while game:
    players = c.input1()
    c.display()
    win = False
    i = 1
    counter = 1
    while not win:
        if r_players=="3":
            if i>3:
                i =1
            if i  == 1:
                currentPlayer = "Player1"
                marker = players[0]
            elif i  == 2:
                currentPlayer = "Player2"
                marker = players[1]
            else:
                currentPlayer = "Player3"
                marker = players[2]
            position = c.choice1()
        else:
            if i>2:
                i =1
            if i  == 1:
                currentPlayer = "Player1"
                marker = players[0]
            else:
                currentPlayer = "Player2"
                marker = players[1]
            position = c.choice1()
        if not c.play(position, marker):
            print(f"Column {position} full")
        reversedBoard = c.board1()
        if c.check_rows(marker) or c.check_rows(marker, reversedBoard) or c.check_cols(marker):
            win = True
            c.display()
            print("================================")
            print(f"Game won by {currentPlayer}")
            print("================================")
       
            replay = input("Do you want to play again (Y/N) ? ")
            if replay[0].lower() == 'n':
                game = False
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("Game ended !")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            else:       
                c = Connect_game()
            break
        elif counter==mul:
            c.display()
            print("================================")
            print(f"Game is Draw ")
            print("================================")
       
            replay = input("Do you want to play again (Y/N) ? ")
            if replay[0].lower() == 'n':
                game = False
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
                print("Game ended !")
                print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
            else:       
                c = Connect_game()
            break
        c.display()
        i += 1
        counter +=1