# Tutorial https://pythonprogramming.net/adding-score-pygame-video-game/
# https://stackoverflow.com/questions/41332861/click-and-drag-a-rectangle-with-pygame

# Rules:
# Dodge the snowflakes
# Single user wins at 55
# Multi user wins at 35
# Computer wins at 150
# To go in pause mode or to exit pause mode click esc
# To change to full-screen display click f, to exit full-screen display press n
# (this can be done just in game loop or intro)

import pygame
import time
import random

pygame.init()

# Setting Window size
display_width = 1000
display_height = 552

# Organising Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 205)
yellow = (255, 255, 0)

# Pixel Width of the image
usr_width = 81

# Disable pause function
pause = False
# Disable win function
win = False

# Creating window and personalization
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Avalanche escape!')  # Adding game caption description
clock = pygame.time.Clock()

# Setting game image icon
gameIcon = pygame.image.load('object.jpg')
pygame.display.set_icon(gameIcon)

# Setting a game picture for the users  male use keyboard, female mouse
usrImg = pygame.image.load('user.png')
grlUsr = pygame.image.load('girl.png')

# Setting game background image
background_image_filename = 'Background.jpg'
background = pygame.image.load(background_image_filename).convert()

# Adding quick sound when the character is hit by an object
crash_sound = pygame.mixer.Sound("gameover.wav")
# Adding quick sound when the user wins!
win_sound = pygame.mixer.Sound("win.wav")


# Counting the number of objects avoided, if avoided 35 you win! Multi player
def obj_avoided(count):
    global win
    font = pygame.font.SysFont(None, 25)
    text = font.render("Avoided: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))
    if count == 35:  # Game winning condition
        win = True
        game_win()


# Counting the number of objects avoided, if avoided 55 you win! Single player
def obj_avoided_single(count):
    global win
    font = pygame.font.SysFont(None, 25)
    text = font.render("Avoided: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))
    if count == 55:  # Game winning condition
        win = True
        game_win_single()


# Computer wins at 150!
def obj_avoided_comp(count):
    global win
    font = pygame.font.SysFont(None, 25)
    text = font.render("Avoided: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))
    if count == 150:  # Game winning condition
        win = True
        game_win_comp()


# Defining object to avoid
def obj(objstartx,objstarty):
    avoidobjname = 'object.jpg'
    avoidobj = pygame.image.load(avoidobjname).convert()
    gameDisplay.blit(avoidobj,(objstartx,objstarty))


# User object
def user(x, y):
    gameDisplay.blit(usrImg, (x, y))


# Select font color black and size
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# Select font color red and size
def text_objects_collision(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


# Print out when there is a collision, for Multi-player
def crash():
    largeText = pygame.font.Font('freesansbold.ttf', 125)
    TextSurf, TextRect = text_objects_collision('Collision!', largeText)
    TextRect.center = ((display_width / 2), (display_height / 3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.mixer.Sound.play(crash_sound)  # Adding quick sound
    pygame.mixer.music.stop()

    pygame.display.update()

    time.sleep(2)

    game_loop()


# Crash function for single user mode
def crash_single():
    largeText = pygame.font.Font('freesansbold.ttf', 125)
    TextSurf, TextRect = text_objects_collision('Collision!', largeText)
    TextRect.center = ((display_width / 2), (display_height / 3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.mixer.Sound.play(crash_sound)  # Adding quick sound
    pygame.mixer.music.stop()

    pygame.display.update()

    time.sleep(2)

    game_loop_single()


# Crash function for computer
def crash_comp():
    largeText = pygame.font.Font('freesansbold.ttf', 125)
    TextSurf, TextRect = text_objects_collision('Collision!', largeText)
    TextRect.center = ((display_width / 2), (display_height / 3))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.mixer.Sound.play(crash_sound)  # Adding quick sound
    pygame.mixer.music.stop()

    pygame.display.update()

    time.sleep(2)

    game_loop_comp()


# Define a function to exit the game using a button
def exitgame():
    pygame.quit()
    quit()


# Make a button
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


# Resume the game after pausing
def resume():
    global pause
    pygame.mixer.music.unpause() # Resume music when exiting pause mode and coming back to the game
    pause = False


# Adding Pausing Option
def paused():

    global pause

    pygame.mixer.music.pause()  # Pause music while in pause mode

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # Click esc to exit pause mode and come back in the game
                if event.key == pygame.K_ESCAPE:
                    resume()

        button("Continue", 205, 365, 150, 80, green, blue, resume)  # Buttons same as intro
        button("Exit", 645, 365, 150, 80, red, blue, exitgame)
        button("Change game mode", 380, 455, 240, 80, white, blue, game_intro)

        largeText = pygame.font.SysFont("freesansbold.ttf", 115)   # Write paused message on screen
        TextSurf, TextRect = text_objects_collision("Paused", largeText)
        TextRect.center = ((display_width / 2), (display_height / 5))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(90)


# Win function for single user
def game_win_single():
    win = True

    pygame.mixer.Sound.play(win_sound) # Adding quick sound, repeat just once
    pygame.mixer.music.play(0)
    pygame.mixer.music.stop()

    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play again", 205, 365, 150, 80, green, blue, game_loop_single)  # Buttons same as intro
        button("Exit", 645, 365, 150, 80, red, blue, exitgame)
        button("Change game mode", 380, 455, 240, 80, white, blue, game_intro)

        largeText = pygame.font.SysFont("freesansbold.ttf", 115)  # Write paused message on screen
        TextSurf, TextRect = text_objects_collision("You won!!!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 5))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(90)


# Win function for multi-player
def game_win():
    win = True

    pygame.mixer.Sound.play(win_sound)  # Adding quick sound, repeat just once
    pygame.mixer.music.play(0)
    pygame.mixer.music.stop()

    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play again", 205, 365, 150, 80, green, blue, game_loop)  # Buttons same as intro
        button("Exit", 645, 365, 150, 80, red, blue, exitgame)
        button("Change game mode", 380, 455, 240, 80, white, blue, game_intro)  # ???

        largeText = pygame.font.SysFont("freesansbold.ttf", 115)  # Write paused message on screen
        TextSurf, TextRect = text_objects_collision("You won!!!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 5))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(90)


# Win function for computer playing
def game_win_comp():
    win = True

    pygame.mixer.Sound.play(win_sound)  # Adding quick sound, repeat just once
    pygame.mixer.music.play(0)
    pygame.mixer.music.stop()

    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play again", 205, 365, 150, 80, green, blue, game_loop_comp)  # Buttons same as intro
        button("Exit", 645, 365, 150, 80, red, blue, exitgame)
        button("Change game mode", 380, 455, 240, 80, white, blue, game_intro)  # ???

        largeText = pygame.font.SysFont("freesansbold.ttf", 115)  # Write paused message on screen
        TextSurf, TextRect = text_objects_collision("You won!!!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 5))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()
        clock.tick(90)


# Make a game menu
def game_intro():

    intro = True

    global gameDisplay # Used to enable/disable full-screen mode

    # While intro is true execute the code
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # When pressing a button do...
                if event.key == pygame.K_f:  # When pressing the f key enable full-screen mode
                    gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
                if event.key == pygame.K_n:  # When pressing the n key disable full-screen mode
                    gameDisplay = pygame.display.set_mode((display_width, display_height))

        # Setting menu background picture
        intro_image_filename = 'intro.jpg'
        intro_image = pygame.image.load(intro_image_filename).convert()
        gameDisplay.blit(intro_image, (0, 0))

        # Writing game introduction
        largeText = pygame.font.SysFont("freesansbold.ttf", 100)
        TextSurf, TextRect = text_objects("Avalanche escape!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 5))
        gameDisplay.blit(TextSurf, TextRect)
        medText = pygame.font.SysFont("freesansbold.ttf", 50)
        TextSurf, TextRect = text_objects("Avoid the snowflakes to survive the winter storm", medText)
        TextRect.center = ((display_width / 2), (display_height / 3.2))
        gameDisplay.blit(TextSurf, TextRect)

        # Place the buttons,1 label, 2,3 coordinates where to place it, 4,5 button width and length, 6,7 color and
        # hover color, 8 action to execute when pressed. We call the button function to do that
        button("Multi-Player", 205, 305, 170, 80, green, blue, game_loop)
        button("Single-player", 645, 305, 170, 80, red, blue, game_loop_single)
        button("Computer-play", 400, 235, 220, 80, white, blue, game_loop_comp)
        button("Game instructions", 395, 375, 230, 80, yellow, blue, game_instr)
        # Is important to choose the button position right otherwise there is a risk bug overlapping

        pygame.display.update()
        clock.tick(90)


# Make an instruction menu
def game_instr():

    introexp = True

    global gameDisplay  # Used to enable/disable full-screen mode

    # While intro is true execute the code
    while introexp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:  # When pressing a button do...
                if event.key == pygame.K_f:  # When pressing the f key enable full-screen mode
                    gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
                if event.key == pygame.K_n:  # When pressing the n key disable full-screen mode
                    gameDisplay = pygame.display.set_mode((display_width, display_height))

        # Setting instruction background picture
        intro_image_filename = 'instra.jpg'
        intro_image = pygame.image.load(intro_image_filename).convert()
        gameDisplay.blit(intro_image, (0, 0))

        # Writing instruction menu heading and the rules
        largeText = pygame.font.SysFont("freesansbold.ttf", 100)
        TextSurf, TextRect = text_objects("Instructions", largeText)
        TextRect.center = ((display_width / 2), (display_height / 6))
        gameDisplay.blit(TextSurf, TextRect)
        medText = pygame.font.SysFont("freesansbold.ttf", 38)
        TextSurf, TextRect = text_objects("1) Use the keyboard arrows to move the boy and the mouse to move the "
                                              "girl ", medText)
        TextRect.center = ((display_width / 2), (display_height / 3.3))
        gameDisplay.blit(TextSurf, TextRect)
        medText = pygame.font.SysFont("freesansbold.ttf", 38)
        TextSurf, TextRect = text_objects("2) Single user wins at 55, Multi user wins at 35, "
                                          "Computer wins at 150 ", medText)
        TextRect.center = ((display_width / 2), (display_height / 2.7))
        gameDisplay.blit(TextSurf, TextRect)
        medText = pygame.font.SysFont("freesansbold.ttf", 38)
        TextSurf, TextRect = text_objects("3) To go in pause mode or to exit pause mode press esc", medText)
        TextRect.center = ((display_width / 2), (display_height / 2.3))
        gameDisplay.blit(TextSurf, TextRect)
        medText = pygame.font.SysFont("freesansbold.ttf", 38)
        TextSurf, TextRect = text_objects("4) To change to full-screen display press F, "
                                          "to exit full-screen display press N ", medText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        medText = pygame.font.SysFont("freesansbold.ttf", 38)
        TextSurf, TextRect = text_objects("(this can be done, while playing, in the menu and here)", medText)
        TextRect.center = ((display_width / 2), (display_height / 1.75))
        gameDisplay.blit(TextSurf, TextRect)

        # Place the buttons,1 label, 2,3 coordinates where to place it, 4,5 button width and length, 6,7 color and
        # hover color, 8 action to execute when pressed. We call the button function to do that
        button("Back to menu", 380, 345, 240, 80, red, blue, game_intro)
        # Is important to choose the button position right otherwise there is a risk bug overlapping

        pygame.display.update()
        clock.tick(90)


# Main loop game, multi-player
def game_loop():

    pygame.mixer.music.load('Zelda.wav')  # Setting musing to play during the game
    pygame.mixer.music.play(-1) # Repeat this song forever

    # Positioning the user at the center lower end of the screen
    x = (display_width * 0.3)
    y = (display_height * 0.8)

    # Keeping track on the x and y movements of the user on the screen
    x_change = 0
    y_change = 0

    # Make the object start in a random x position of the screen and above the y coordinates, setting initial speed
    objstartx = random.randrange(0, display_width)
    abjstarty = -400
    objspeed = 3

    # Image used for the object height*width
    objheight = 80
    objwidth = 80

    # Counting the number of objects avoided
    avoided = 0

    user_drag = False
    girl_user = grlUsr.get_rect(center=(display_width * 0.72, display_height * 0.88))

    global pause

    global gameDisplay # Used to enable/disable full-screen mode

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit program when clicking X
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:  # When pressing a button do...
                if event.key == pygame.K_LEFT:  # When pressing the left or right key move left or right
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_ESCAPE: # Press esc to pause the game
                    pause = True # Turning pause to true enable the paused while loop
                    paused()
                    # Press esc to pause the game
                if event.key == pygame.K_ESCAPE and (pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN):
                    pause = True # Turning pause to true enable the paused while loop
                    paused()
                    x_change = 0  # Avoid the if someone pause the game while moving, the character will
                    y_change = 0  # not automatically keep moving when resuming the game
                if event.key == pygame.K_UP:  # When pressing the up and down keys move up or down
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.type == pygame.KEYDOWN:  # When pressing a button do...
                    if event.key == pygame.K_f:  # When pressing the f key enable full-screen mode
                        gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
                    if event.key == pygame.K_n:  # When pressing the n key disable full-screen mode
                        gameDisplay = pygame.display.set_mode((display_width, display_height))

            if event.type == pygame.KEYUP:   # When stopping pressing the arrows, do nothing
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

            if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse controls for the girl user
                if event.button == 1: # If pressing the left mouse button
                    if girl_user.collidepoint(event.pos): # If pressing on the girl rectangle image
                        user_drag = True
                        mouse_x, mouse_y = event.pos   # Calculate the offset of where the image
                        offset_x = girl_user.x - mouse_x  # is getting dragged by the mouse
                        offset_y = girl_user.y - mouse_y

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # When the user stops pressing the left mouse button stop updating the
                    user_drag = False  # drag position

            if event.type == pygame.MOUSEMOTION:
                if user_drag:  # If the user is dragging the girl image update the position of the girl image
                    mouse_x, mouse_y = event.pos  # to where the mouse is going
                    girl_user.x = mouse_x + offset_x
                    girl_user.y = mouse_y + offset_y

        x += x_change # Update the x position of the user after movement
        y += y_change # Update the y position of the user after movement

        gameDisplay.blit(background, (0, 0)) # Enabling game background on the screen

        obj(objstartx,abjstarty) # Enabling the object on the screen
        # Making vary the y position of the object every time a new abject comes in the screen by the speed value
        abjstarty += objspeed

        # Display on the scree the girl user (mouse user)
        gameDisplay.blit(grlUsr, girl_user)

        user(x, y) # Enabling user on the screen
        obj_avoided(avoided) # Display on the screen the number of avoided objects

        # If user tries to move outside of the window alert collision, in x direction
        if x > display_width - usr_width or x < 0:
            crash()
        # If user tries to move outside of the window alert collision, in y direction
        if y > display_height - usr_width or y < 0:
            crash()

        # If user tries to move outside of the window alert collision, in x direction girl user
        if girl_user.x > display_width - usr_width or girl_user.x < 0:
            crash()
        # If user tries to move outside of the window alert collision, in y direction girl user
        if girl_user.y > display_height - usr_width or girl_user.y < 0:
            crash()

        # Once the object goes off the screen, start another object
        if abjstarty > display_height:
            abjstarty = 0 - objwidth  # Make the object start closer on the Y axis to increase difficulty
            objstartx = random.randrange(0, display_width) # Make initial x position of object be always different
            avoided += 1 # Increase counter of avoided objects
            objspeed += 0.4 # Increase speed of the object

        # Declare conditions necessary to flag the collision happened
        if y < abjstarty + objheight and y > abjstarty or y + usr_width > abjstarty \
                and y + usr_width < abjstarty + objwidth:
            if x > objstartx and x < objstartx + objwidth or x + usr_width > objstartx \
                    and x + usr_width < objstartx + objwidth:
                crash()

        # Declare conditions necessary to flag the collision happened for girl user
        if girl_user.y < abjstarty + objheight and girl_user.y > abjstarty or girl_user.y + usr_width > abjstarty \
                and girl_user.y + usr_width < abjstarty + objwidth:
            if girl_user.x > objstartx and girl_user.x < objstartx + objwidth or girl_user.x + usr_width > objstartx \
                    and girl_user.x + usr_width < objstartx + objwidth:
                crash()

        pygame.display.update() # Keep updating display every loop iteration
        clock.tick(90) # Frame per second


# Main loop game, single user
def game_loop_single():

    pygame.mixer.music.load('Zelda.wav')  # Setting musing to play during the game
    pygame.mixer.music.play(-1) # Repeat this song forever

    # Make the object start in a random x position of the screen and above the y coordinates, setting initial speed
    objstartx = random.randrange(0, display_width)
    abjstarty = -400
    objspeed = 3

    # Image used for the object height*width
    objheight = 80
    objwidth = 80

    # Counting the number of objects avoided
    avoided = 0

    x_change = 0
    y_change = 0

    user_drag = False
    boy_user = usrImg.get_rect(center=(display_width * 0.5, display_height * 0.88))

    global pause

    global gameDisplay # Used to Enable/disable full-screen mode

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit program when clicking X
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse controls for the girl user
                if event.button == 1: # If pressing the left mouse button
                    if boy_user.collidepoint(event.pos): # If pressing on the girl rectangle image
                        user_drag = True
                        mouse_x, mouse_y = event.pos   # Calculate the offset of where the image
                        offset_x = boy_user.x - mouse_x  # is getting dragged by the mouse
                        offset_y = boy_user.y - mouse_y

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # When the user stops pressing the left mouse button stop updating the
                    user_drag = False  # drag position

            if event.type == pygame.MOUSEMOTION:
                if user_drag:  # If the user is dragging the girl image update the position of the girl image
                    mouse_x, mouse_y = event.pos  # to where the mouse is going
                    boy_user.x = mouse_x + offset_x
                    boy_user.y = mouse_y + offset_y

            if event.type == pygame.KEYDOWN:  # When pressing a button do...
                if event.key == pygame.K_LEFT:  # When pressing the left or right key move left or right
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_ESCAPE:  # Press esc to pause the game
                    pause = True  # Turning pause to true enable the paused while loop
                    paused()
                if event.key == pygame.K_ESCAPE and (pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN):
                    # Press esc to pause the game
                    pause = True  # Turning pause to true enable the paused while loop
                    paused()
                    x_change = 0  # Avoid the if someone pause the game while moving, the character will
                    y_change = 0  # not automatically keep moving when resuming the game
                if event.key == pygame.K_UP:  # When pressing the up and down keys move up or down
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.type == pygame.KEYDOWN:  # When pressing a button do...
                    if event.key == pygame.K_f:  # When pressing f key set full-screen mode
                        gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
                    if event.key == pygame.K_n:  # When pressing n key set the standard mode
                        gameDisplay = pygame.display.set_mode((display_width, display_height))

            if event.type == pygame.KEYUP:  # When stopping pressing the arrows, do nothing
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change = 0

        boy_user.x += x_change  # Update the x position of the user after movement
        boy_user.y += y_change

        gameDisplay.blit(background, (0, 0)) # Enabling game background on the screen

        obj(objstartx,abjstarty) # Enabling the object on the screen
        # Making vary the y position of the object every time a new abject comes in the screen by the speed value
        abjstarty += objspeed

        # Display on the scree the girl user (mouse user)
        gameDisplay.blit(usrImg, boy_user)

        obj_avoided_single(avoided) # Display on the screen the number of avoided objects

        # If user tries to move outside of the window alert collision, in x direction girl user
        if boy_user.x > display_width - usr_width or boy_user.x < 0:
            crash_single()
        # If user tries to move outside of the window alert collision, in y direction girl user
        if boy_user.y > display_height - usr_width or boy_user.y < 0:
            crash_single()

        # Once the object goes off the screen, start another object
        if abjstarty > display_height:
            abjstarty = 0 - objwidth  # Make the object start closer on the Y axis to increase difficulty
            objstartx = random.randrange(0, display_width) # Make initial x position of object be always different
            avoided += 1 # Increase counter of avoided objects
            objspeed += 0.4 # Increase speed of the object

        # Declare conditions necessary to flag the collision happened for girl user
        if boy_user.y < abjstarty + objheight and boy_user.y > abjstarty or boy_user.y + usr_width > abjstarty \
                and boy_user.y + usr_width < abjstarty + objwidth:
            if boy_user.x > objstartx and boy_user.x < objstartx + objwidth or boy_user.x + usr_width > objstartx \
                    and boy_user.x + usr_width < objstartx + objwidth:
                crash_single()

        pygame.display.update()  # Keep updating display every loop iteration
        clock.tick(90)  # Frame per second


# Main loop game, computer playing
def game_loop_comp():

    pygame.mixer.music.load('Zelda.wav')  # Setting musing to play during the game
    pygame.mixer.music.play(-1) # Repeat this song forever

    # Make the object start in a random x position of the screen and above the y coordinates, setting initial speed
    objstartx = random.randrange(0, display_width)
    abjstarty = -400
    objspeed = 3

    # Image used for the object height*width
    objheight = 80
    objwidth = 80

    # Counting the number of objects avoided
    avoided = 0

    global gameDisplay # To enable/disable full-screen

    boy_user = usrImg.get_rect(center=(display_width * 0.5, display_height * 0.88))

    global pause  # Adding flags to switch mode.
    global flag   # The character start dodging objects going from left to right,
    global flag2  # Once arrived at the end of the screen it reverse it's direction
    flag = True   # Can do that continuously
    flag2 = False # The flags are used later to switch if statements to switch direction

    gameExitc = False

    while not gameExitc:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Exit program when clicking X
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Press esc to pause the game
                    pause = True  # Turning pause to true enable the paused while loop
                    paused()
                if event.key == pygame.K_ESCAPE and (pygame.K_LEFT or pygame.K_RIGHT or pygame.K_UP or pygame.K_DOWN):
                    # Press esc to pause the game
                    pause = True  # Turning pause to true enable the paused while loop
                    paused()
                if event.type == pygame.KEYDOWN:  # When pressing a button do...
                    if event.key == pygame.K_f:  # When pressing the f key, set full-screen mode
                        gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
                    if event.key == pygame.K_n:  # When pressing the n key set the standard mode
                        gameDisplay = pygame.display.set_mode((display_width, display_height))

        gameDisplay.blit(background, (0, 0)) # Enabling game background on the screen

        obj(objstartx,abjstarty) # Enabling the object on the screen
        # Making vary the y position of the object every time a new abject comes in the screen by the speed value
        abjstarty += objspeed

        # Display on the scree the girl user (mouse user)
        gameDisplay.blit(usrImg, boy_user)

        obj_avoided_comp(avoided) # Display on the screen the number of avoided objects

        # Once the object goes off the screen, start another object
        if abjstarty > display_height:
            abjstarty = 0 - objwidth  # Make the object start closer on the Y axis to increase difficulty
            objstartx = random.randrange(0, display_width)  # Make initial x position of object be always different
            avoided += 1  # Increase counter of avoided objects
            objspeed += 0.4  # Increase speed of the object

        if flag == True:
            # If the falling object is on the same x coordinates of the character, go to next if statement
            if objstartx - 80 <= boy_user.x < objstartx + 80 and abjstarty < display_height:
                # If the user can move to left, avoiding the object and not going off the screen proceed
                if 160 < boy_user.x <= (display_width - 160):
                    x_change = 20
                    boy_user.x += x_change
                # If the user reach end of the screen reverse direction to avoid the object and change for loop to
                # change permanently direction (I do that using the flag)
                else:
                    x_change = -60
                    boy_user.x += x_change
                    flag2 = True
                    flag = False
        # Now the user moves from left to right dodging the objects, till reach end of the screen, then direction is
        # reversed and changed if statement to the one used before(always using flags)
        if flag2 == True:
            if objstartx - 80 <= boy_user.x < objstartx + 80 and abjstarty < display_height:
                if 160 < boy_user.x <= (display_width - 160):
                    x_change = -20
                    boy_user.x += x_change
                else:
                    x_change = +60
                    boy_user.x += x_change
                    flag = True
                    flag2 = False

        # If user tries to move outside of the window alert collision, in x direction girl user
        if boy_user.x > display_width - usr_width or boy_user.x < 0:
            crash_comp()
        # If user tries to move outside of the window alert collision, in y direction girl user
        if boy_user.y > display_height - usr_width or boy_user.y < 0:
            crash_comp()

        # Declare conditions necessary to flag the collision happened for girl user
        if boy_user.y < abjstarty + objheight and boy_user.y > abjstarty or boy_user.y + usr_width > abjstarty \
                and boy_user.y + usr_width < abjstarty + objwidth:
            if boy_user.x > objstartx and boy_user.x < objstartx + objwidth or boy_user.x + usr_width > objstartx \
                    and boy_user.x + usr_width < objstartx + objwidth:
                crash_comp()

        pygame.display.update()  # Keep updating display every loop iteration
        clock.tick(90)  # Frame per second


game_intro()
pygame.quit()
quit()