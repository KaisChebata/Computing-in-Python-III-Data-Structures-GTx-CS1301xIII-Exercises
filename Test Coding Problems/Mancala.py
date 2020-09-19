#The game Mancala is one of the oldest games in recorded
#history. You can read more about it here:
#https://www.thesprucecrafts.com/how-to-play-mancala-409424
#
#For this problem, though, you don't need to know how to
#play the game. All you need to know is the board layout
#and the conditions for winning.
#
#A Mancala board is made of two rows of 6 cups, with two
#bigger cups at the ends. Each cup holds some number of
#stones or chips. For our purposes, though, we'll include
#the bigger cups at the end of the corresponding rows.
#
#So, for us, a Mancala board is represented as a
#2-dimensional list of integers. Each item in the lists
#represents a cup, and the number represents how many
#stones are currently in that cup. For example, this
#could be one board:
#
# [[5, 3, 0, 2, 6, 8, 1],
#  [1, 6, 8, 0, 4, 1, 4]]
#
#With this board representation, the game is over when
#every cup is empty except the top left and the bottom
#right. When the game is over, whoever has more stones
#in their cup wins: if the top left has more stones, the
#top player wins. If the bottom right has more stones,
#the bottom player wins.
#
#Write a function called check_winner. check_winner takes
#as a 2-dimensional list representing a game board. You
#may assume list will always have two lists, each with
#7 items, corresponding to the board structure shown
#above.
#
#Your function should return one of four strings
#depending on the values of the list:
#
# - If the game is not over (that is, there are stones
#   in any bucket except for the top-left or bottom-
#   right), return "Keep playing!"
# - If the game is over and the top player wins (that is,
#   there are more stones in top-left than bottom-right),
#   return "Player 1 wins!"
# - If the game is over and the bottom player wins (that
#   is, there are more stones in the bottom-right than
#   the top-left), return "Player 2 wins!"
# - If the game is over but the score is tied (that is,
#   there is an equal number of stones in the top-left
#   and bottom-right), return "Draw!"


#Write your function here!

def check_winner(board):
    # solution 1
    # player1, player2 = board
    # player1_flag = player1[1:] == [0, 0, 0, 0, 0, 0]
    # player2_flag = player2[:-1] == [0, 0, 0, 0, 0, 0]

    # if not (player1_flag or player2_flag):
    #     return 'Keep playing!'
    # elif player1_flag and player2_flag and player1[0] > player2[6]:
    #     return 'Player 1 wins!'
    # elif player1_flag and player2_flag and player1[0] < player2[6]:
    #     return 'Player 2 wins!'
    # else:
    #     return 'Draw!'

    # solution 2
    if (sum(board[0][1:]) != 0) or (sum(board[1][:-1]) != 0):
        return 'Keep playing!'
    elif board[0][0] == board[1][-1]:
        return 'Draw!'
    elif board[0][0] > board[1][-1]:
        return 'Player 1 wins!'
    else:
        return 'Player 2 wins!'
#Below are some lines of code that will test your function.
#You can change the value of the variable(s) to test your
#function with different inputs.
#
#If your function works correctly, this will originally
#print:
#Keep playing!
#Player 1 wins!
#Player 2 wins!
#Draw!
keep_playing = [[5, 3, 0, 2, 6, 8, 1], [1, 6, 8, 0, 4, 1, 4]]
player1_wins = [[27, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 21]]
player2_wins = [[16, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 32]]
game_is_tied = [[24, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 24]]
print(check_winner(keep_playing))
print(check_winner(player1_wins))
print(check_winner(player2_wins))
print(check_winner(game_is_tied))
