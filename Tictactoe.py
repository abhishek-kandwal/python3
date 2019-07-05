# this is the tic tac toe game
# importing the clear_output from IPython.display for clearing the output screen.

from IPython.display import clear_output

# initializating the variables here

board = ['#','1','2','3','4','5','6','7','8','9']
player1 = ''
player2 = ''
counter = 0
chance = ''
won = 0

# this play_board function prints the updated tic tac toe board 

def play_board(board):
    clear_output()  
    print('HERE IS YOUR tic tac toe board: \n')
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    if won == 0:
        moves()

# this function will check who is the winner player 1 or player 2

def winner_checker():
    global won
    if (board[1] == player1 and board[2] == player1 and board[3] == player1) or (board[4] == player1 and board[5] == player1 and board[6] == player1) or (board[7] == player1 and board[8] == player1 and board[9] == player1) or (board[1] == player1 and board[5] == player1 and board[9] == player1) or (board[3] == player1 and board[5] == player1 and board[7] == player1) or (board[9] == player1 and board[6] == player1 and board[3] == player1) or (board[2] == player1 and board[5] == player1 and board[8] == player1) or (board[1] == player1 and board[4] == player1 and board[7] == player1):
        clear_output()
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(f'PLAYER 1 has won the tic tac toe match {player1}')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        won += 1
        replay() 
    elif (board[1] == player2 and board[2] == player2 and board[3] == player2) or (board[4] == player2 and board[5] == player2 and board[6] == player2) or (board[7] == player2 and board[8] == player2 and board[9] == player2) or (board[1] == player2 and board[5] == player2 and board[9] == player2) or (board[3] == player2 and board[5] == player2 and board[7] == player2) or (board[9] == player2 and board[6] == player2 and board[3] == player2) or (board[2] == player2 and board[5] == player2 and board[8] == player2) or (board[1] == player2 and board[4] == player2 and board[7] == player2):
        clear_output()
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        print(f'PLAYER 2 has won the tic tac toe match {player2}')
        print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        won += 1
        replay()
    else:
        play_board(board)

# moves function update the board according to the players move 

def moves():
    global board
    global counter
    global chance
    move = int(input('enter your box no: (1 to 9) of yout choice ' + chance + ' \t'))
    if counter%2 == 0:
        board[move] = player1
        counter+=1
        chance = 'PLAYER 2 -> ' + player2
        winner_checker()
    else:
        board[move] = player2
        counter+=1
        chance = 'PLAYER 1 -> ' + player1
        winner_checker()

# start_game function will starts the game according to the players choice

def start_game(con):
    if con.lower() =="yes" or con.lower() == 'no':
        if con.lower() =="yes":
            player_tag()
        else:
            game_end()
    else:
        clear_output()
        start()

# player_tag function will give player1 or player2 x or o tag.

def player_tag():
    global chance
    tag = input('choose a tag: x or o \t')
    if tag.lower() == 'x' or tag.lower() == 'o':        
        global player1
        global player2
        player1 = tag.lower()
        chance = 'PLAYER 1 -> ' + player1
        if player1 == 'x':
            player2 = 'o'
        else:
            player2 = 'x'
        play_board(board)

    else:
        player_tag()

# game_end function will finish the game.

def game_end():
    clear_output()
    print('thank you')
    start()

# start function will take the input from the player to start the game or not 

def start():
    con = input('do you want to play tic tac toe : YES or NO \t')
    clear_output()
    start_game(con)

# replay function will restart the game for play.

def replay():
    global board
    global player1
    global player2
    global counter
    board = ['#','1','2','3','4','5','6','7','8','9']
    player1 = ''
    player2 = ''
    counter = 0
    start()

# starting the game

start()
