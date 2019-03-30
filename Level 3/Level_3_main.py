import random

WIDTH = 800
HEIGHT = 600
GAP = 130
SPEED = 3
GRAVITY = 0.3
FLAP_VELOCITY = 40

turtle = Actor('ship', (75, 200))
trash1 = Actor('sixpackrings', anchor=('center', 'center'))

def draw():
    screen.blit('ocean1', (0, 0))
    #screen.draw.text("boi" , color='white', midtop=(WIDTH//2, 40), fontsize=70)

    trash1.draw()

    turtle.draw()

# Initial state of the bird
turtle.dead = False

def on_key_down():
    if keyboard.up:
        turtle.y -= FLAP_VELOCITY
    if keyboard.down:
        turtle.y += FLAP_VELOCITY

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

def reset_trash():
    trash1.pos = (WIDTH, random.randint(40,HEIGHT-40))

def update_trash():
    trash1.left -= SPEED
    if trash1.right < 0:
        reset_trash()




reset_trash()

def update():

    update_trash()
    update_turtle()

