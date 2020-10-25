# PyGame library to create the game board and redraw when the board needs to be updated -- event listener
import pygame
pygame.init()

# Reference https://realpython.com/pygame-a-primer/

pygame.display.set_caption('Tic Tac Toe') 

# Define constants for the screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Images -- image directory -> add more avatars
player1 = pygame.image.load("images/player1.png")
player2 = pygame.image.load("images/player2.png")

# Provide the screen to the user
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Gameboard array to keep track of whether or not there is an open slot
gameboard = [[None, None, None],
             [None, None, None],
             [None, None, None]]

# player == 0 if player 1 ("X")
# player == 1 if player 2 ("0")
def handleClick(player):
    currentPosition = pygame.mouse.get_pos()

    x_pos = currentPosition[0]
    y_pos = currentPosition[1]
    # Box 1 (top left)
    if (x_pos < SCREEN_WIDTH / 3 and y_pos < SCREEN_WIDTH / 3):
        if not player and gameboard[0][0] is None:
            gameboard[0][0] = "X"
            #print("draw x")
            # drawX(position)
        elif player and gameboard[0][0] is None:
            gameboard[0][0] = "O"
            #print("draw o")
            # drawO(position)

    # Box 2 (middle top)
    elif (SCREEN_WIDTH / 3 < x_pos < SCREEN_WIDTH * (2/3) and y_pos < SCREEN_WIDTH / 3):
        if not player and gameboard[0][1] is None:
            gameboard[0][1] = "X"
            # drawX(position)
        elif player and gameboard[0][1] is None:
            gameboard[0][1] = "O"
            # drawO(position)

    # Box 3 (top right)
    elif (SCREEN_WIDTH * (2/3) < x_pos and y_pos < SCREEN_WIDTH / 3):
        if not player and gameboard[0][2] is None:
            gameboard[0][2] = "X"
            # drawX(position)
        elif player and gameboard[0][2] is None:
            gameboard[0][2] = "O"
            # drawO(position)

    # Box 4 (middle left)
    elif (x_pos < SCREEN_WIDTH / 3 and SCREEN_WIDTH / 3 < y_pos < SCREEN_WIDTH * (2/3)):
        if not player and gameboard[1][0] is None:
            gameboard[1][0] = "X"
            # drawX(position)
        elif player and gameboard[1][0] is None:
            gameboard[1][0] = "O"
            # drawO(position)

    # Box 5 (middle middle)
    elif (SCREEN_WIDTH / 3 < x_pos < SCREEN_WIDTH * (2/3) and SCREEN_WIDTH / 3 < y_pos < SCREEN_WIDTH * (2/3)):
        if not player and gameboard[1][1] is None:
            gameboard[1][1] = "X"
            # drawX(position)
        elif player and gameboard[1][1] is None:
            gameboard[1][1] = "O"
            # drawO(position)

    # Box 6 (middle right)
    elif (SCREEN_WIDTH * (2/3) < x_pos and SCREEN_WIDTH / 3 < y_pos < SCREEN_WIDTH * (2/3)):
        if not player and gameboard[1][2] is None:
            gameboard[1][2] = "X"
            # drawX(position)
        elif player and gameboard[1][2] is None:
            gameboard[1][2] = "O"
            # drawO(position)

    # Box 7 (bottom left)
    elif (x_pos < SCREEN_WIDTH / 3 and SCREEN_WIDTH * (2/3) < y_pos):
        if not player and gameboard[2][0] is None:
            gameboard[2][0] = "X"
            # drawX(position)
        elif player and gameboard[2][0] is None:
            gameboard[2][0] = "O"
            # drawO(position)

    # Box 8 (bottom middle)
    elif (SCREEN_WIDTH / 3 < x_pos < SCREEN_WIDTH * (2/3) and SCREEN_WIDTH * (2/3) < y_pos):
        if not player and gameboard[2][1] is None:
            gameboard[2][1] = "X"
            # drawX(position)
        elif player and gameboard[2][1] is None:
            gameboard[2][1] = "O"
            # drawO(position)

    # Box 9 (bottom right)
    elif (SCREEN_WIDTH * (2/3) < x_pos and SCREEN_WIDTH * (2/3) < y_pos):
        if not player and gameboard[2][2] is None:
            gameboard[2][2] = "X"
            # drawX(position)
        elif player and gameboard[2][2] is None:
            gameboard[2][2] = "O"
            # drawO(position)

    print(gameboard)

def checkVictory():
    # Check for row victory
    for row in range(3):
        if gameboard[row][0] == gameboard[row][1] and gameboard[row][1] == gameboard[row][2] and gameboard[row][0] != None:
            print('victory in row')
            print(str(gameboard[row][0]) + ' wins the game')
            return True
    
    # Check for column victory
    for col in range(3):
        if gameboard[0][col] == gameboard[1][col] and gameboard[1][col] == gameboard[2][col] and gameboard[0][col] != None:
            print('victory in col')
            print(str(gameboard[0][row]) + ' wins the game')
            return True

    # Check for diagonal victory
    if gameboard[0][0] == gameboard[1][1] and gameboard[1][1] == gameboard[2][2] and gameboard[0][0] != None:
        print('victory in diagonal')
        print(str(gameboard[0][0]) + ' wins the game')
        return True
    elif gameboard[0][2] == gameboard[1][1] and gameboard[1][1] == gameboard[2][0] and gameboard[0][2] != None:
        print('victory in diagonal')
        print(str(gameboard[0][2]) + ' wins the game')
        return True
    
    return False
    
def clear():
    global gameboard
    gameboard = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]

def playerDisplay():
    screen.blit(player1, (100,0))
    screen.blit(player2, (300, 0))
    
        
# Run pygame until user quits
running = True
currentPlayer = False  # starts with player 1 (X)
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Check if user pressed the mouse down -- next deal with spawning "X" or "O"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse (x, y) pos and check if they are valid aka its a click within the square
            # Also need to check if that square is filled already
            handleClick(currentPlayer)
            currentPlayer = not currentPlayer
    
    # Check for victory
    if (checkVictory()):
        clear()

    # Fill the background with white
    # (R, G, B)
    screen.fill((255, 255, 255))
    playerDisplay()

    # LATER Make cool start screen
    # LATER player chooses
    # LATER play again?
    # LATER music?

    # Create a 3x3 grid aka the game board
    # Horizontal lines
    pygame.draw.line(screen, (0, 0, 0), (0, SCREEN_WIDTH / 3), (SCREEN_WIDTH, SCREEN_WIDTH / 3), 10)
    pygame.draw.line(screen, (0, 0, 0), (0, SCREEN_WIDTH * (2 / 3)), (SCREEN_WIDTH, SCREEN_WIDTH * (2 / 3)), 10)
    # Vertical lines
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH / 3, 0), (SCREEN_WIDTH / 3, SCREEN_WIDTH), 10)
    pygame.draw.line(screen, (0, 0, 0), (SCREEN_WIDTH * (2 / 3), 0), (SCREEN_WIDTH * (2 / 3), SCREEN_WIDTH), 10)
    
    # Flip the display
    pygame.display.update()