import random

WIDTH = 1000
HEIGHT = 800
SPEED = 3
VELOCITY = 40

turtle = Actor('player1',       (75, HEIGHT//2) )
trash1 = Actor('sixpackrings', (WIDTH, ( random.randint(0,HEIGHT)    )))
trash2 = Actor('straw',         (WIDTH, ( random.randint(0,HEIGHT)   )))
trash3 = Actor('plasticbag',     (WIDTH, ( random.randint(0,HEIGHT)  )))
trash4 = Actor('plasticbottle', (WIDTH, ( random.randint(0,HEIGHT)   )))
trash5 = Actor('can', (WIDTH, ( random.randint(0,HEIGHT)   )))
shark1 = Actor('shark', (WIDTH, ( random.randint(0,HEIGHT))))
shark2 = Actor('shark', (WIDTH, ( random.randint(0,HEIGHT))))
net = Actor('net', (WIDTH, ( random.randint(0,HEIGHT))))

# Initial state of the turtle
turtle.dead = False
turtle.x = 75
count=0
game_active = False
game_level = 1


def blackscreen():
    screen.fill((0,0,0))
    screen.draw.text("Press space to play a game!", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)

def draw():
    global game_active
    global game_level
    if game_active:
        if game_level == 1:
            screen.blit('ocean1', (0, 0))
            trash1.draw()
            trash2.draw()
            trash3.draw()
            trash4.draw()
            trash5.draw()
            turtle.draw()
        elif game_level == 2:
            screen.blit('coralreef', (0, 0))
            shark1.draw()
            shark2.draw()
            net.draw()
            turtle.draw()

        elif game_level == 3:
            x = 0
        elif game_level == 4:
            x = 0
        screen.draw.text(str(count), color='white' , midtop=(WIDTH-50,HEIGHT-70),fontsize=60)
    elif game_active == False:
        blackscreen()



def check_count():
    global count
    global game_level
    if count >= 5:
        count = 0
        game_level = game_level + 1



def on_key_down():
    global game_active
    global count
    global SPEED
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
        SPEED=3
        if turtle.dead:
            turtle.dead = False
            reset_turtle()
    if keyboard.escape:
        game_active = False
        SPEED=0
        count=0


def update_turtle():
    global game_active
    if game_level==1:
        if turtle.colliderect(trash1) or turtle.colliderect(trash2) or turtle.colliderect(trash3) or turtle.colliderect(trash4) or turtle.colliderect(trash5):
            turtle.image = 'player1dead'
            game_active = 0
            reset_turtle()
            reset_trash()
    elif game_level==2
        if turtle.colliderect(shark1) or turtle.colliderect(shark2) or turtle.colliderect(net):
            turtle.image = 'player1dead'
            game_active = 0
            reset_turtle()
            reset_sharknet()


    if not 0 < turtle.top:
        turtle.top=1
    elif not turtle.bottom < HEIGHT:
        turtle.bottom=HEIGHT-1
    if not 0 < turtle.left:
        turtle.left=1
    elif not turtle.right < WIDTH:
        turtle.right=WIDTH


def reset_turtle():
    turtle.pos = (75, HEIGHT//2)
    turtle.image = 'player1'
    turtle.dead = False


def reset_trash1():
    trash1.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_trash2():
    trash2.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_trash3():
    trash3.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_trash4():
    trash4.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_trash5():
    trash5.pos = (WIDTH, random.randint(40,HEIGHT-40))



def update_trash():
    global count
    trash1.x -= SPEED+1
    trash2.x -= SPEED
    trash3.x -= SPEED-1
    trash4.x -= SPEED+0.5
    trash5.x -= SPEED-0.5
    if trash1.right < 0:
        reset_trash1()
        count+=1
        check_count()
    if trash2.right < 0:
        reset_trash2()
        count+=1
    if trash3.right < 0:
        reset_trash3()
        count+=1
    if trash4.right < 0:
        reset_trash4()
        count+=1
    if trash5.right < 0:
        reset_trash5()
        count+=1

def reset_trash():
    reset_trash1()
    reset_trash2()
    reset_trash3()
    reset_trash4()
    reset_trash5()


def update():
   global game_level
   update_turtle()
   if game_level==1:
        update_trash()
    elif game_level==2:
        update_sharknet()

