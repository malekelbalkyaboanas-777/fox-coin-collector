# importing random because we will use it in randoming place of coin.
import random
# importing sys because we will use it to bring the screen of game over and to close the program.
import sys
# importing pgzrun to run all the code below according to pgzrun syntax.
import pgzrun
# importing all builtin modules in pgzrun to make "visual studio code" to ensure and suggest written modules in the program.
from pgzero.builtins import *

# Identification of fox, coin and game over pictures to certain variables and any other variables.
Fox = Actor("fox")
Fox.pos = 100,100
Coin = Actor("coin")
Coin.pos = 250,250
game_over = Actor("game_over")
game_over.pos = 250,250
score = 0
is_game_over = False  # making variable "is_game_over" to help in game over's screen and exiting from program

# Identifying the dimentiones of the screen
WIDTH = 500
HEIGHT = Fox.height + 420

# Draw function including all displaying mehods and making to options (in game and when game_over) according to if statement.
def draw():
    screen.clear() 
    if is_game_over: # while game is over.
        screen.blit('space', (0, 0))
        game_over.draw() # to display image of game_over
        screen.draw.text(f"Total Score: {score}", center=(250, 400), fontsize=40, color="white") # To display score.
        
    else: # While in game.
        screen.blit('background', (0, 0))
        Fox.draw()
        Coin.draw()
        screen.draw.text(f"Score: {score} ", (10,10) , color = "white", fontsize = 30 )
     
# Update function including all replacing coin, actions when fox is out of screen and keyboard actions.
def update():
    global score # to edit on the variable score at the first of code.
    if not is_game_over:
        # Keyboard actions
        if keyboard.left:
            Fox.x -= 3
        if keyboard.right:
            Fox.x += 3
        if keyboard.up:
            Fox.y -= 3
        if keyboard.down:
            Fox.y += 3
        # To make the fox not out of the screen by x and y coordinates.
        if Fox.x > WIDTH:
            Fox.x = 0
        elif Fox.x < 0:
            Fox.x = WIDTH
        if Fox.y > HEIGHT:
            Fox.y = 0
        elif Fox.y < 0:
            Fox.y = HEIGHT
        # actions when fox collid coin(including randoming palce of coin and increasing score by one).
        if Fox.colliderect(Coin):
            score += 1
            Coin.x = random.randint(1, WIDTH -1)    
            Coin.y = random.randint(1, HEIGHT - 1)

# Making function end_game(including making is_game_over = true and exiting from program through 3 seconds)
def end_game():
    global is_game_over
    is_game_over = True
    clock.schedule(sys.exit, 3)

# making game_over in 10 seconds
clock.schedule(end_game, 10)  

pgzrun.go() # To translate and apply all codes before.
