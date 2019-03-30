import random

WIDTH = 800
HEIGHT = 600
SPEED = 3
VELOCITY = 40

turtle = Actor('player1', (75, HEIGHT//2))
trash1 = Actor('sixpackrings', anchor=('center', 'center'))
trash2 = Actor('straw', anchor=('center', 'center'))
trash3 = Actor('plasticbag', anchor=('center', 'center'))
trash4 = Actor('plasticbottle', anchor=('center', 'center'))
count = 0

game_active = False
game_level = 1

def draw():
    global game_active
    if game_active:
        screen.blit('ocean1', (0, 0))
        trash1.draw()
        trash2.draw()
        trash3.draw()
        trash4.draw()
        turtle.draw()
        screen.draw.text(str(count), color='white' , midtop=(WIDTH-50,HEIGHT-70),fontsize=60)
    else:
        screen.fill((0,0,0))
        screen.draw.text("Press space to play a game!", (300, 300), fontsize=32)

# Initial state of the bird
turtle.dead = False
turtle.x = 75


def on_key_down():
    global game_active
    if not turtle.dead:
        if keyboard.up:
            turtle.y -= VELOCITY
        if keyboard.down:
            turtle.y += VELOCITY
        if keyboard.left:
            turtle.x -= VELOCITY
        if keyboard.right:
            turtle.x += VELOCITY
    if keyboard.space:
        game_active = True
        turtle.dead = False
        reset_turtle()
    if keyboard.escape:
        game_active = False


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


def reset_turtle():
    turtle.pos = (turtle.x, 300)
    turtle.image = 'player1'

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

def update():
    update_trash()
    update_turtle()