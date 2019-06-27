import pyautogui
import pygame
import time

pygame.init()

# Setting Window size
display_width = 2000
display_height = 1552

# Organising Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 205)
yellow = (255, 255, 0)

# Creating window and personalization
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Imitate the image')  # Adding game caption description
clock = pygame.time.Clock()

# Setting game background image
background_image_filename = 'back.jpg'
background = pygame.image.load(background_image_filename).convert()

# Setting game image icon
gameIcon = pygame.image.load('ico.png')
pygame.display.set_icon(gameIcon)


# Taking a screenshot and taking and saving it in an image
def picture():
    pic = pyautogui.screenshot()
    pic.save('screenshot.png')


# Select font color red and size
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


# Print out when someone drags a block outside the canvas area
def crash():
    largeText = pygame.font.Font('freesansbold.ttf', 125)
    TextSurf, TextRect = text_objects('Outside screen!', largeText)
    TextRect.center = ((display_width / 2), (display_height / 3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


# Print out an error when more than 6 squares are selected for player
def endgame():
    largeText = pygame.font.Font('freesansbold.ttf', 125)
    TextSurf, TextRect = text_objects('Select maximum 6 squares', largeText)
    TextRect.center = ((display_width / 2), (display_height / 3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


# Making a button
def button(msg, x, y, w, h, hc, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # Determining when the mouse hover on the rectangles area
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:  # If user hover on the rectangle area and click execute button command
            action()
    else:
        pygame.draw.rect(gameDisplay, hc, (x, y, w, h))  # If user hover on button and doesn't click change button color

    smallText = pygame.font.SysFont("freesansbold.ttf",35)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


# Main loop game
def game_loop():

    # Setting width of the squares to detect if they fall outside canvas
    objwidth = 200

    # Setting flags for activating and deactivating drag and drop of squares
    user_drag = False
    user_drag11 = False
    user_drag12 = False
    user_drag13 = False
    user_drag14 = False
    user_drag15 = False
    user_drag2 = False
    user_drag21 = False
    user_drag22 = False
    user_drag23 = False
    user_drag24 = False
    user_drag25 = False

    # Loading square image and making a rectangle to enclose each square (children squares)
    objpic = pygame.image.load('square.png')
    objpos = objpic.get_rect(center=(200, 300))
    objpic11 = pygame.image.load('square.png')
    objpos11 = objpic11.get_rect(center=(400, 650))
    objpic12 = pygame.image.load('square.png')
    objpos12 = objpic12.get_rect(center=(display_width/8, display_height/2))
    objpic13 = pygame.image.load('square.png')
    objpos13 = objpic13.get_rect(center=(display_width/3, display_height/6))
    objpic14 = pygame.image.load('square.png')
    objpos14 = objpic14.get_rect(center=(display_width/4, display_height/4))
    objpic15 = pygame.image.load('square.png')
    objpos15 = objpic15.get_rect(center=(display_width/3, display_height/1.8))

    # Loading square image and making a rectangle to enclose each square (parent squares)
    objpic2 = pygame.image.load('square.png')
    objpos2 = objpic2.get_rect(center=(display_width/1.5, display_height / 2))
    objpic21 = pygame.image.load('square.png')
    objpos21 = objpic21.get_rect(center=(display_width / 1.5, display_height / 4))
    objpic22 = pygame.image.load('square.png')
    objpos22 = objpic22.get_rect(center=(display_width / 1.2, display_height / 2))
    objpic23 = pygame.image.load('square.png')
    objpos23 = objpic23.get_rect(center=(display_width /1.1, display_height / 4))
    objpic24 = pygame.image.load('square.png')
    objpos24 = objpic24.get_rect(center=(display_width / 1.5, display_height / 3))
    objpic25 = pygame.image.load('square.png')
    objpos25 = objpic25.get_rect(center=(display_width / 1.2, display_height / 5))

    gameExit = False

    # Setting variables to load multiple squares simultaneously
    i =0
    j=0

    gameDisplay.blit(background, (0, 0))  # Enabling game background on the screen

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit program when clicking X
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse controls for squares and Canvas 1/2 buttons
                if event.button == 1:  # If pressing the left mouse button
                    if canvas1btn.collidepoint(event.pos):  # Pressing Canvas 1 square button
                        i = i +1  # Keeping record of how many times the button has been pressed
                        print("i", i)
                    if canvas2btn.collidepoint(event.pos):  # Pressing Canvas 2 square button
                        j = j+ 1  # Keeping record of how many times the button has been pressed
                        print("j", j)
                    if objpos.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag = True
                        mouse_x, mouse_y = event.pos   # Calculate the offset of where the image
                        offset_x = objpos.x - mouse_x  # is getting dragged by the mouse
                        offset_y = objpos.y - mouse_y
                    if objpos11.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag11 = True
                        mouse_x11, mouse_y11 = event.pos   # Calculate the offset of where the image
                        offset_x11 = objpos11.x - mouse_x11  # is getting dragged by the mouse
                        offset_y11 = objpos11.y - mouse_y11
                    if objpos12.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag12 = True
                        mouse_x12, mouse_y12 = event.pos   # Calculate the offset of where the image
                        offset_x12 = objpos12.x - mouse_x12  # is getting dragged by the mouse
                        offset_y12 = objpos12.y - mouse_y12
                    if objpos13.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag13 = True
                        mouse_x13, mouse_y13 = event.pos   # Calculate the offset of where the image
                        offset_x13 = objpos13.x - mouse_x13  # is getting dragged by the mouse
                        offset_y13 = objpos13.y - mouse_y13
                    if objpos14.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag14 = True
                        mouse_x14, mouse_y14 = event.pos   # Calculate the offset of where the image
                        offset_x14 = objpos14.x - mouse_x14  # is getting dragged by the mouse
                        offset_y14 = objpos14.y - mouse_y14
                    if objpos15.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag15 = True
                        mouse_x15, mouse_y15 = event.pos   # Calculate the offset of where the image
                        offset_x15 = objpos15.x - mouse_x15  # is getting dragged by the mouse
                        offset_y15 = objpos15.y - mouse_y15
                    if objpos2.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag2 = True
                        mouse_x2, mouse_y2 = event.pos   # Calculate the offset of where the image
                        offset_x2 = objpos2.x - mouse_x2  # is getting dragged by the mouse
                        offset_y2 = objpos2.y - mouse_y2
                    if objpos21.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag21 = True
                        mouse_x21, mouse_y21 = event.pos   # Calculate the offset of where the image
                        offset_x21 = objpos21.x - mouse_x21  # is getting dragged by the mouse
                        offset_y21 = objpos21.y - mouse_y21
                    if objpos22.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag22 = True
                        mouse_x22, mouse_y22 = event.pos   # Calculate the offset of where the image
                        offset_x22 = objpos22.x - mouse_x22  # is getting dragged by the mouse
                        offset_y22 = objpos22.y - mouse_y22
                    if objpos23.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag23 = True
                        mouse_x23, mouse_y23 = event.pos   # Calculate the offset of where the image
                        offset_x23 = objpos23.x - mouse_x23  # is getting dragged by the mouse
                        offset_y23 = objpos23.y - mouse_y23
                    if objpos24.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag24 = True
                        mouse_x24, mouse_y24 = event.pos   # Calculate the offset of where the image
                        offset_x24 = objpos24.x - mouse_x24  # is getting dragged by the mouse
                        offset_y24 = objpos24.y - mouse_y24
                    if objpos25.collidepoint(event.pos): # If pressing on the square rectangle image
                        user_drag25 = True
                        mouse_x25, mouse_y25 = event.pos   # Calculate the offset of where the image
                        offset_x25 = objpos25.x - mouse_x25  # is getting dragged by the mouse
                        offset_y25 = objpos25.y - mouse_y25

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # When the user stops pressing the left mouse button stop updating the
                    user_drag = False  # drag position
                    user_drag11 = False
                    user_drag12 = False
                    user_drag13 = False
                    user_drag14 = False
                    user_drag15 = False
                    user_drag2 = False
                    user_drag21 = False
                    user_drag22 = False
                    user_drag23 = False
                    user_drag24 = False
                    user_drag25 = False

            if event.type == pygame.MOUSEMOTION:
                if user_drag:  # If the user is dragging the square image update the position of the square image
                    mouse_x, mouse_y = event.pos  # to where the mouse is going
                    objpos.x = mouse_x + offset_x
                    objpos.y = mouse_y + offset_y
                if user_drag11:  # If the user is dragging the square image update the position of the square image
                    mouse_x11, mouse_y11 = event.pos  # to where the mouse is going
                    objpos11.x = mouse_x11 + offset_x11
                    objpos11.y = mouse_y11 + offset_y11
                if user_drag12:  # If the user is dragging the square image update the position of the square image
                    mouse_x12, mouse_y12 = event.pos  # to where the mouse is going
                    objpos12.x = mouse_x12 + offset_x12
                    objpos12.y = mouse_y12 + offset_y12
                if user_drag13:  # If the user is dragging the square image update the position of the square image
                    mouse_x13, mouse_y13 = event.pos  # to where the mouse is going
                    objpos13.x = mouse_x13 + offset_x13
                    objpos13.y = mouse_y13 + offset_y13
                if user_drag14:  # If the user is dragging the square image update the position of the square image
                    mouse_x14, mouse_y14 = event.pos  # to where the mouse is going
                    objpos14.x = mouse_x14 + offset_x14
                    objpos14.y = mouse_y14 + offset_y14
                if user_drag15:  # If the user is dragging the square image update the position of the square image
                    mouse_x15, mouse_y15 = event.pos  # to where the mouse is going
                    objpos15.x = mouse_x15 + offset_x15
                    objpos15.y = mouse_y15 + offset_y15
                if user_drag2:  # If the user is dragging the square image update the position of the square image
                    mouse_x2, mouse_y2 = event.pos  # to where the mouse is going
                    objpos2.x = mouse_x2 + offset_x2
                    objpos2.y = mouse_y2 + offset_y2
                if user_drag21:  # If the user is dragging the square image update the position of the square image
                    mouse_x21, mouse_y21 = event.pos  # to where the mouse is going
                    objpos21.x = mouse_x21 + offset_x21
                    objpos21.y = mouse_y21 + offset_y21
                if user_drag22:  # If the user is dragging the square image update the position of the square image
                    mouse_x22, mouse_y22 = event.pos  # to where the mouse is going
                    objpos22.x = mouse_x22 + offset_x22
                    objpos22.y = mouse_y22 + offset_y22
                if user_drag23:  # If the user is dragging the square image update the position of the square image
                    mouse_x23, mouse_y23 = event.pos  # to where the mouse is going
                    objpos23.x = mouse_x23 + offset_x23
                    objpos23.y = mouse_y23 + offset_y23
                if user_drag24:  # If the user is dragging the square image update the position of the square image
                    mouse_x24, mouse_y24 = event.pos  # to where the mouse is going
                    objpos24.x = mouse_x24 + offset_x24
                    objpos24.y = mouse_y24 + offset_y24
                if user_drag25:  # If the user is dragging the square image update the position of the square image
                    mouse_x25, mouse_y25 = event.pos  # to where the mouse is going
                    objpos25.x = mouse_x25 + offset_x25
                    objpos25.y = mouse_y25 + offset_y25

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos.x > display_width/2 - objwidth or objpos.x < 0:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos.y > display_height - objwidth or objpos.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos2.x > display_width - objwidth or objpos2.x < display_width/2:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos2.y > display_height - objwidth or objpos2.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos11.x > display_width/2 - objwidth or objpos11.x < 0:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos11.y > display_height - objwidth or objpos11.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos12.x > display_width/2 - objwidth or objpos12.x < 0:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos12.y > display_height - objwidth or objpos12.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos13.x > display_width/2 - objwidth or objpos13.x < 0:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos13.y > display_height - objwidth or objpos13.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos14.x > display_width/2 - objwidth or objpos14.x < 0:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos14.y > display_height - objwidth or objpos14.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos15.x > display_width/2 - objwidth or objpos15.x < 0:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos15.y > display_height - objwidth or objpos15.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos21.x > display_width - objwidth or objpos21.x < display_width/2:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos21.y > display_height - objwidth or objpos21.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos22.x > display_width - objwidth or objpos22.x < display_width/2:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos22.y > display_height - objwidth or objpos22.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos23.x > display_width - objwidth or objpos23.x < display_width/2:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos23.y > display_height - objwidth or objpos23.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos24.x > display_width - objwidth or objpos24.x < display_width/2:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos24.y > display_height - objwidth or objpos24.y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction square user
        if objpos25.x > display_width - objwidth or objpos25.x < display_width/2:
            crash()
        # If user tries to move outside of the window alert collision, in y direction square user
        if objpos25.y > display_height - objwidth or objpos25.y < 0:
            crash()

        gameDisplay.blit(background, (0, 0))  # Enabling game background on the screen

        # Making a button to be used to load squares for Canvas 1
        btnpic = pygame.image.load('btn1.png')
        canvas1btn = btnpic.get_rect(center=(765, 1265))
        gameDisplay.blit(btnpic, canvas1btn)
        # Making a button to be used to load squares for Canvas 2
        btnpic2 = pygame.image.load('btn2.png')
        canvas2btn = btnpic2.get_rect(center=(1265, 1265))
        gameDisplay.blit(btnpic2, canvas2btn)
        # Drawing a line at the centre of the window to divide the two canvases
        pygame.draw.line(gameDisplay, black, (1000, 0), (1000, 1550), 9)
        # Making a button to take a screen-shot of the game result
        button("Save", 880, 1355, 240, 80, yellow, blue, picture)

        # Keeping count of how many times the Canvas 1 squares button is pressed and creating as many squares
        if i==1:
            gameDisplay.blit(objpic, objpos)
        if i==2:
            gameDisplay.blit(objpic, objpos)
            gameDisplay.blit(objpic11, objpos11)
        if i==3:
            gameDisplay.blit(objpic, objpos)
            gameDisplay.blit(objpic11, objpos11)
            gameDisplay.blit(objpic12, objpos12)
        if i==4:
            gameDisplay.blit(objpic, objpos)
            gameDisplay.blit(objpic11, objpos11)
            gameDisplay.blit(objpic12, objpos12)
            gameDisplay.blit(objpic13, objpos13)
        if i==5:
            gameDisplay.blit(objpic, objpos)
            gameDisplay.blit(objpic11, objpos11)
            gameDisplay.blit(objpic12, objpos12)
            gameDisplay.blit(objpic13, objpos13)
            gameDisplay.blit(objpic14, objpos14)
        if i==6:
            gameDisplay.blit(objpic, objpos)
            gameDisplay.blit(objpic11, objpos11)
            gameDisplay.blit(objpic12, objpos12)
            gameDisplay.blit(objpic13, objpos13)
            gameDisplay.blit(objpic14, objpos14)
            gameDisplay.blit(objpic15, objpos15)

        # Keeping count of how many times the Canvas 1 squares button is pressed and creating as many squares
        if j==1:
            gameDisplay.blit(objpic2, objpos2)
        if j==2:
            gameDisplay.blit(objpic2, objpos2)
            gameDisplay.blit(objpic21, objpos21)
        if j==3:
            gameDisplay.blit(objpic2, objpos2)
            gameDisplay.blit(objpic21, objpos21)
            gameDisplay.blit(objpic22, objpos22)
        if j==4:
            gameDisplay.blit(objpic2, objpos2)
            gameDisplay.blit(objpic21, objpos21)
            gameDisplay.blit(objpic22, objpos22)
            gameDisplay.blit(objpic23, objpos23)
        if j==5:
            gameDisplay.blit(objpic2, objpos2)
            gameDisplay.blit(objpic21, objpos21)
            gameDisplay.blit(objpic22, objpos22)
            gameDisplay.blit(objpic23, objpos23)
            gameDisplay.blit(objpic24, objpos24)
        if j==6:
            gameDisplay.blit(objpic2, objpos2)
            gameDisplay.blit(objpic21, objpos21)
            gameDisplay.blit(objpic22, objpos22)
            gameDisplay.blit(objpic23, objpos23)
            gameDisplay.blit(objpic24, objpos24)
            gameDisplay.blit(objpic25, objpos25)

        # If the user tries to create more than 6 squares for each canvas an error is prompt
        if j>6 or i>6:
            endgame()

        pygame.display.update()  # Keep updating display every loop iteration
        clock.tick(90)  # Frame per second

game_loop()
pygame.quit()
quit()