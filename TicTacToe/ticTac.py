#Implementation of Two Player Tic-Tac-Toe game in Python.
def printBoard(board, update, CallbackContext):
    b0, b1, b2, b3, b4, b5, b6, b7, b8 = board['0'], board['1'], board['2'], board['3'], board['4'], board['5'], board['6'], board['7'], board['8']  
    
    update.message.reply_text(f'{b0}\t|\t{b1}\t|\t{b2}\n{b3}\t|\t{b4}\t|\t{b5}\n{b6}\t|\t{b7}\t|\t{b8}')
    

# Now we'll write the main function which has all the gameplay functionality.
def game(Board, board_keys, update, CallbackContext):

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(Board, update, CallbackContext)
        update.message.reply_text("Du bist dran," + turn + ".Wähle ein Feld?")

        move = input()        

        if Board[move] == ' ':
            Board[move] = turn
            count += 1
        else:
            update.message.reply_text("Der Platz ist bereits belegt.\nWas möchtest du stattdessen wählen?")
            continue
        
        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if Board['0'] == Board['1'] == Board['2'] != ' ': # across the top
                printBoard(Board)
                update.message.reply_text("\nGame Over.\n")                
                update.message.reply_text(" **** " +turn + " won. ****")                
                break
            elif Board['3'] == Board['4'] == Board['5'] != ' ': # across the middle
                printBoard(Board)
                update.message.reply_text("\nGame Over.\n")                
                update.message.reply_text(" **** " +turn + " won. ****")
                break
            elif Board['6'] == Board['7'] == Board['8'] != ' ': # across the bottom
                printBoard(Board)
                update.message.reply_text("\nGame Over.\n")                
                update.message.reply_text(" **** " +turn + " won. ****")
                break
            elif Board['0'] == Board['3'] == Board['6'] != ' ': # down the left side
                printBoard(Board)
                update.message.reply_text("\nGame Over.\n")                
                update.message.reply_text(" **** " +turn + " won. ****")
                break
            elif Board['1'] == Board['4'] == Board['7'] != ' ': # down the middle
                printBoard(Board)
                update.message.reply_text("\nGame Over.\n")                
                update.message.reply_text(" **** " +turn + " won. ****")
                break
            elif Board['2'] == Board['5'] == Board['8'] != ' ': # down the right side
                printBoard(Board)
                update.message.reply_text("\nGame Over.\n")                
                update.message.reply_text(" **** " +turn + " won. ****")
                break 
            elif Board['0'] == Board['4'] == Board['8'] != ' ': # diagonal
                printBoard(Board)
                update.message.reply_text("\nGame Over.\n")                
                update.message.reply_text(" **** " +turn + " won. ****")
                break
            elif Board['6'] == Board['4'] == Board['2'] != ' ': # diagonal
                printBoard(Board)
                update.message.reply_text("\nGame Over.\n")                
                update.message.reply_text(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            update.message.reply_text("\nGame Over.\n")                
            update.message.reply_text("Unendschieden!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Willst du nochmal spielen?(j/n)")
    if restart == "j" or restart == "Y":  
        for key in board_keys:
            Board[key] = " "

        game()

if __name__ == "__main__":
    game(Board, board_keys, update, CallbackContext)