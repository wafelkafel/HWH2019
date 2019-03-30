import random

WIDTH = 800
HEIGHT = 600
SPEED = 30
VELOCITY = 40

turtle = Actor('player1',       (75, HEIGHT//2) )
trash1 = Actor('sixpackrings', (WIDTH, ( random.randint(0,HEIGHT)    )))
trash2 = Actor('straw',         (WIDTH, ( random.randint(0,HEIGHT)   )))
trash3 = Actor('plasticbag',     (WIDTH, ( random.randint(0,HEIGHT)  )))
trash4 = Actor('plasticbottle', (WIDTH, ( random.randint(0,HEIGHT)   )))
count=0

def draw():
    screen.blit('ocean1', (0, 0))
    trash1.draw()
    trash2.draw()
    trash3.draw()
    trash4.draw()
    turtle.draw()
    screen.draw.text(str(count), color='white' , midtop=(WIDTH-50,HEIGHT-70),fontsize=60)

# Initial state of the bird
turtle.dead = False
turtle.x = 75


def on_key_down():
    gameactive=1
    if keyboard.up:
        turtle.y -= VELOCITY
    if keyboard.down:
        turtle.y += VELOCITY
    if keyboard.left:
        turtle.x -= VELOCITY
    if keyboard.right:
        turtle.x += VELOCITY


def update_turtle():

    if turtle.colliderect(trash1) or turtle.colliderect(trash2) or turtle.colliderect(trash3) or turtle.colliderect(trash4):
        turtle.dead = True
        turtle.image = 'player1dead'

    if not 0 < turtle.top:
        turtle.top=1
    elif not turtle.bottom < HEIGHT:
        turtle.bottom=HEIGHT-1

    if not 0 < turtle.left:
        turtle.left=1
    elif not turtle.right < WIDTH:
        turtle.right=WIDTH

def reset_trash1():
    trash1.pos = (WIDTH, random.randint(40,HEIGHT-40))


def reset_trash2():
    trash2.pos = (WIDTH, random.randint(40,HEIGHT-40))


def reset_trash3():
    trash3.pos = (WIDTH, random.randint(40,HEIGHT-40))


def reset_trash4():
    trash4.pos = (WIDTH, random.randint(40,HEIGHT-40))


def update_trash():
    global count
    trash1.x -= SPEED+1
    trash2.x -= SPEED
    trash3.x -= SPEED-1
    trash4.x -= SPEED+0.5

    if trash1.right < 0:
        reset_trash1()
        count+=1

    if trash2.right < 0:
        reset_trash2()
        count+=1

    if trash3.right < 0:
        reset_trash3()
        count+=1

    if trash4.right < 0:
        reset_trash4()
        count+=1

def update_speed():
    global count
    global SPEED
    if (count % 20 == 0) & (count!=0):
        SPEED=2+SPEED

def update():
    update_trash()
    update_turtle()
    update_speed()
    global SPEED
    print(str(SPEED))
