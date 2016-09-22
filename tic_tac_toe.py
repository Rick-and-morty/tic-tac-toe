
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 1, 2, 3, 4, 5, 6, 7, 8, 9

board = {'top-L': '1', 'top-M': '2', 'top-R': '3', 'mid-L': '4', 'mid-M': '5',
         'mid-R': '6', 'low-L': '7', 'low-M': '8', 'low-R': '9'}


def gameboard(board):

    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# placement on the board and invalid moves on the board


def ask_number(letter):
    """Ask for a number within the range 1-9."""
    response = input('which box would you like to choose? ')
# i got this from davis

    if response == "1":
        if board['top-L'] == "X" or board['top-L'] == "O":
            print("non valid move")
        else:
            board['top-L'] = letter
    elif response == "2":
        if board['top-M'] == "X" or board['top-M'] == "O":
            print('non valid move')
        else:
            board['top-M'] = letter
    elif response == "3":
        if board['top-R'] == "X" or board['top-R'] == "O":
            print('non valid move')
        else:
            board['top-R'] = letter
    elif response == "4":
        if board['mid-L'] == "X" or board['mid-L'] == "O":
            print('non valid move')
        else:
            board['mid-L'] = letter
    elif response == "5":
        if board['mid-M'] == "X" or board['mid-M'] == "O":
            print('non valid move')
        else:
            board['mid-M'] = letter
    elif response == "6":
        if board['mid-R'] == "X" or board['mid-R'] == "O":
            print('non valid move')
        else:
            board['mid-R'] = letter
    elif response == "7":
        if board['low-L'] == "X" or board['low-L'] == "O":
            print('non valid move')
        else:
            board['low-L'] = letter
    elif response == "8":
        if board['low-M'] == "X" or board['low-M'] == "O":
            print('non valid move')
        else:
            board['low-M'] = letter
    elif response == "9":
        if board['low-R'] == "X" or board['low-R'] == "O":
            print('non valid move')
        else:
            board['low-R'] = letter


def winning_conditions():

    '''def winning_conditions():'''
"""Winning conditions can be across."""

while True:
    gameboard(board)
    ask_number(X)
    gameboard(board)
    ask_number(O)
