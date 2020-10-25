# PyGame library to create the game board and redraw when the board needs to be updated -- event listener
import pygame
pygame.init()

# Reference https://realpython.com/pygame-a-primer/

pygame.display.set_caption('Tic Tac Toe') 

# Define constants for the screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# Images -- image directory -> add more avatars
player1 = pygame.image.load("images/LOK_Korra.jpg")
player2 = pygame.image.load("images/LOK_Asami.jpg")
background = pygame.image.load("images/startMenu.jpg")

# Provide the screen to the user
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Gameboard array to keep track of whether or not there is an open slot
gameboard = [[None, None, None],
             [None, None, None],
             [None, None, None]]

# Winner
# 0 = Player 1
# 1 = Player 2
# 2 = Scratch
winner = 3

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

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
            # drawX(position)
        elif player and gameboard[0][0] is None:
            gameboard[0][0] = "O"
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
    global winner
    # Check for row victory
    for row in range(3):
        if gameboard[row][0] == gameboard[row][1] and gameboard[row][1] == gameboard[row][2] and gameboard[row][0] != None:
            if gameboard[row][0] == "X":
                winner = 0
            elif gameboard[row][0] == "O":
                winner = 1

            return True
    
    # Check for column victory
    for col in range(3):
        if gameboard[0][col] == gameboard[1][col] and gameboard[1][col] == gameboard[2][col] and gameboard[0][col] != None:
            if gameboard[0][col] == "X":
                winner = 0
            elif gameboard[0][col] == "O":
                winner = 1

            return True

    # Check for diagonal victory
    if gameboard[0][0] == gameboard[1][1] and gameboard[1][1] == gameboard[2][2] and gameboard[0][0] != None:
        if gameboard[1][1] == "X":
            winner = 0
        elif gameboard[1][1] == "O":
            winner = 1

        return True
    elif gameboard[0][2] == gameboard[1][1] and gameboard[1][1] == gameboard[2][0] and gameboard[0][2] != None:
        if gameboard[1][1] == "X":
            winner = 0
        elif gameboard[1][1] == "O":
            winner = 1

        return True
    
    scratch = True
    for row in gameboard:
        for element in row:
            if element is  None:
                scratch = False

    if scratch:
        winner = 2
        return True

    return False
    
def clear():
    global gameboard
    gameboard = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]

# player == 0 if player 1 ("X")
# player == 1 if player 2 ("0")
def drawPlayers():
    for row in range(3):
        for col in range(3):
            if gameboard[col][row] == "X":
                screen.blit(player1, (row * 200 + 25, col * 200 + 25))
            if gameboard[col][row] == "O":
                screen.blit(player2, (row * 200 + 25, col * 200 + 25))
                
def startMenu():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos();
                x_pos = position[0]
                y_pos = position[1]
                
                if 250 < x_pos < 350 and 500 < y_pos < 550:
                    intro = False
                
        screen.blit(background, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 30)
        TextSurf, TextRect = text_objects("Tic Tac Toe, LOK Style", largeText)
        TextRect.center = (300, 100)
        screen.blit(TextSurf, TextRect)

        pygame.draw.rect(screen, (0, 200, 0), (250, 500, 100, 50))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf, textRect = text_objects("Start", smallText)
        textRect.center = (300, 525)
        screen.blit(textSurf, textRect)
        pygame.display.update()

    screen.fill((255, 255, 255))
    playGame()

def gameOver(winner):
    global screen
    pygame.draw.rect(screen, (255, 255, 255), (100, 150, 400, 300))
    pygame.draw.rect(screen, (0, 200, 0), (130, 350, 150, 50))
    pygame.draw.rect(screen, (200, 0, 0), (315, 350, 150, 50))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Quit", smallText)
    textRect.center = (385, 375)
    screen.blit(textSurf, textRect)

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Play again", smallText)
    textRect.center = (200, 375)
    screen.blit(textSurf, textRect)
    pygame.display.update()
    print(winner)
    if winner == 0:
        smallText = pygame.font.Font("freesansbold.ttf", 50)
        textSurf, textRect = text_objects("Player 1 Won!", smallText)
        textRect.center = (300, 250)
        screen.blit(textSurf, textRect)
        pygame.display.update()
    elif winner == 1:
        smallText = pygame.font.Font("freesansbold.ttf", 50)
        textSurf, textRect = text_objects("Player 2 Won!", smallText)
        textRect.center = (300, 250)
        screen.blit(textSurf, textRect)
        pygame.display.update()
    elif winner == 2:
        smallText = pygame.font.Font("freesansbold.ttf", 50)
        textSurf, textRect = text_objects("Nobody Won!", smallText)
        textRect.center = (300, 250)
        screen.blit(textSurf, textRect)
        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos();
                x_pos = position[0]
                y_pos = position[1]
                
                if 315 < x_pos < 465 and 350 < y_pos < 400:
                    running = False
                elif 130 < x_pos < 280 and 350 < y_pos < 400:
                    screen.fill((255, 255, 255))
                    clear()
                    playGame()

# Run pygame until user quits
def playGame():
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
            running = False

        # Fill the background with white
        # (R, G, B)
        screen.fill((255, 255, 255))

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

        drawPlayers()
        # Flip the display
        pygame.display.update()

    gameOver(winner)
    quit()

startMenu()