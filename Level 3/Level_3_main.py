import random

WIDTH = 800
HEIGHT = 600
SPEED = 3
VELOCITY = 40

turtle = Actor('turtle', (75, HEIGHT//2))
trash1 = Actor('sixpackrings', anchor=('center', 'center'))
trash2 = Actor('straw', anchor=('center', 'center'))

def draw():
    screen.blit('ocean1', (0, 0))
    #screen.draw.text("boi" , color='white', midtop=(WIDTH//2, 40), fontsize=70)

    trash1.draw()
    trash2.draw()
    turtle.draw()

# Initial state of the bird
turtle.dead = False

def on_key_down():
    if keyboard.up:
        turtle.y -= VELOCITY
    if keyboard.down:
        turtle.y += VELOCITY

def update_turtle():

    turtle.x = 75

    if turtle.colliderect(trash1):
        turtle.dead = True
        turtle.image = 'birddead'
    if not 0 < turtle.y < 720:
        turtle.y = 200
        turtle.dead = False
        turtle.vy = 0
        reset_trash()

def reset_trash1():
    trash1.pos = (WIDTH, random.randint(40,HEIGHT-40))

def reset_trash2():
    trash2.pos = (WIDTH, random.randint(40,HEIGHT-40))

def update_trash():
    trash1.left -= SPEED
    trash2.left -= SPEED
    if trash1.right < 0:
        reset_trash1()
    if trash2.right < 0:
        reset_trash2()


reset_trash()

def update():

    update_trash()
    update_turtle()

