#In the game tic-tac-toe, two players take turns drawing
#Xs and Os on a 3x3 grid. If one player can place three of
#their symbols side-by-side in a row, column, or diagonal,
#they win the game.
#
#For example:
#
# X Wins:   X Wins:   X Wins:   No Winner:
# X|O|X     O|X|X     O|O|      X|O|O
# -+-+-     -+-+-     -+-+-     -+-+-
# O|O|X     X|O|      X|X|X     O|X|X
# -+-+-     -+-+-     -+-+-     -----
# O|X|X      | |O      | |      X|X|O
#
#Write a function called check_winner. check_winner will
#take one parameter as input, a 2D tuple (that is, a tuple
#of tuples). The 2D tuple represents the game board: each
#smaller tuple in the larger tuple is a row of the board,
#and each item in the smaller tuple is a spot on the
#board. There will always be three tuples in the larger
#tuple, and three items in each of the smaller tuples.
#
#Each item in the smaller tuple will always be one of three
#values: the string "X", the string "O", or the value None.
#
#check_winner should return one of three values: the string
#"X" if X has won the game; the string "O" if O has won the
#game; or the value None if there is no winner. None should
#NOT be the string "None"; it should be the value None,
#like the boolean values True and False.
#
#You may assume a player has won the game if and only if
#the board has three of their symbols in a row: you do not
#need to worry about whether the input is a valid game
#otherwise (e.g. a board of nine Xs still counts as X
#winning). You may assume that there will only be one
#winner per board.
#
#Hint: There are only eight possible places to win (three
#rows, three columns, two diagonals).
#
#Hint 2: If you're comfortable on time, you may want to
#check out the last problem before doing this one. It's
#only worth 1 point, but you might be able to design
#one solution that works for both problems!


#Write your function here!
def check_winner(input_tuple):
    pass

#The code below shows how the tic-tac-toe tuples are
#created and tests your code with three games: one where
#X wins, one where O wins, and one where there is no winner.
#Remember, the line breaks in xwins and owins are optional:
#they're just to make the declarations more readable. They
#could be written the same as nowins.
xwins = (("X", "O", "X"),
         ("O", "O", "X"),
         ("O", "X", "X"))
owins = (("O", "X", "X"),
         ("X", "O", None),
         (None, None, "O"))
nowins = (("X", "O", "O"),("O", "X", "X"),("X", "X", "O"))
print(check_winner(xwins))
print(check_winner(owins))
print(check_winner(nowins))


