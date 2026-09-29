import random
import pgzrun
from pgzero.builtins import *

game_hero = Actor("apple_small")
game_hero.pos = 400,500

WIDTH = 1000
HEIGHT = game_hero.height + 500

def draw():
    screen.clear() 
    game_hero.draw()
    screen.draw.text(f" Try to kick the apple \n         Score is: {score} ", (370,10) , color = "white", fontsize = 40 ) 
    
score = 0
def update():
    game_hero.left += 5
    if game_hero.left > WIDTH:
        game_hero.right = 0

def on_mouse_down(pos):
    global score 
    if  game_hero.collidepoint(pos) :
        print("You got me!")
        game_hero.x = random.randint(50, WIDTH - 50)    
        game_hero.y = random.randint(50, HEIGHT - 50)
        score += 1
    else:
        print("You missed me!, GAME OVER...")
        exit()

pgzrun.go()
