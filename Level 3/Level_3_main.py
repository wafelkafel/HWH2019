import random

WIDTH = 1000
HEIGHT = 800
SPEED = 3
VELOCITY = 40
TARGET = 1

turtle = Actor('player1',       (75, HEIGHT//2) )
shark1 = Actor('shark1', (WIDTH, ( random.randint(0,HEIGHT))), anchor=('left', 'center'))
shark2 = Actor('shark2', (WIDTH, ( random.randint(0,HEIGHT))), anchor=('left', 'center'))
net = Actor('net', (WIDTH, ( random.randint(0,HEIGHT))), anchor=('left', 'center'))
oil1 = Actor('oil1', (WIDTH, ( random.randint(0,HEIGHT))), anchor=('left', 'center'))
oil2 = Actor('oil2', (WIDTH, ( random.randint(0,HEIGHT))), anchor=('left', 'center'))
barrel = Actor('barrel', (WIDTH, ( random.randint(0,HEIGHT))), anchor=('left', 'center'))
trash1 = Actor('sixpackrings', (WIDTH, ( random.randint(0,HEIGHT)    )), anchor=('left', 'center'))
trash2 = Actor('straw',         (WIDTH, ( random.randint(0,HEIGHT)   )), anchor=('left', 'center'))
trash3 = Actor('plasticbag',     (WIDTH, ( random.randint(0,HEIGHT)  )), anchor=('left', 'center'))
trash4 = Actor('plasticbottle', (WIDTH, ( random.randint(0,HEIGHT)   )), anchor=('left', 'center'))
trash5 = Actor('can', (WIDTH, ( random.randint(0,HEIGHT)   )), anchor=('left', 'center'))

# Initial state of the turtle
turtle.dead = False
turtle.x = 75
count=0
game_active = False
game_level = 1
slide = 1
escape = False

def blackscreen():
    screen.fill((0,0,0))
def presstoplay():
    screen.draw.text("Press space to play a game!", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
def presstocontinue():
    screen.draw.text("Press space to continue", midtop=(WIDTH//2, HEIGHT-100), fontsize=26)
def youlost():
    screen.draw.text("Sad fact", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
    screen.draw.text("Press space to try again or escape to exit the game", midtop=(WIDTH//2, HEIGHT-100), fontsize=26)

def draw():
    global game_active
    global game_level
    if game_active:
        if game_level == 1:
            screen.blit('coralreef', (0, 0))
            shark1.draw()
            shark2.draw()
            net.draw()
            turtle.draw()
        elif game_level == 2:
            screen.blit('oceantop', (0,0))
            turtle.image = 'turtletop'
            oil1.draw()
            oil2.draw()
            barrel.draw()
            turtle.draw()
        elif game_level == 3:
            screen.blit('ocean1', (0, 0))
            turtle.image = 'player1'
            trash1.draw()
            trash2.draw()
            trash3.draw()
            trash4.draw()
            trash5.draw()
            turtle.draw()
        elif game_level == 4:
            x = 0
        screen.draw.text(str(count), color='white' , midtop=(WIDTH-50,HEIGHT-70),fontsize=60)
    elif game_active == False:
        if slide==1:
            blackscreen()
            screen.draw.text("Year 2005", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
            presstocontinue()
        elif slide==2:
            blackscreen()
            screen.draw.text("First bunch of text", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
            presstocontinue()
        elif slide==3:
            blackscreen()
            screen.draw.text("Second bunch of text", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
            presstocontinue()
        elif slide==4:
            blackscreen()
            presstoplay()
        elif slide==99:
            blackscreen()
            youlost()
        elif slide==6:
            blackscreen()
            screen.draw.text("Year 2010", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
            presstocontinue()
        elif slide==7:
            blackscreen()
            screen.draw.text("Third bunch of text", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
            presstocontinue()
        elif slide==8:
            blackscreen()
            presstoplay()



def check_count():
    global count
    global game_level
    global slide
    if count >= TARGET:
        count = 0
        game_level+=1
        game_active = False
        slide+=1

def checkforactive():
    global game_active
    if game_active:
        SPEED=3
        if turtle.dead:
            turtle.dead = False
            reset_turtle()
            if game_level==1:
                reset_sharknet()
            elif game_level==2:
                reset_oilbarrel()
            elif game_level==3:
                reset_trash()

def checkturtledead():
    global slide
    global count
    global game_active
    if turtle.dead:
        slide=99
        game_active=False
        count=0


def on_key_down():
    global game_active
    global count
    global SPEED
    global slide
    if not turtle.dead:
        if keyboard.up:
            turtle.y -= VELOCITY
        if keyboard.down:
            turtle.y += VELOCITY
        if keyboard.left:
            turtle.x -= VELOCITY
        if keyboard.right:
            turtle.x += VELOCITY
    if slide == 99:
        if keyboard.space:
            reset_turtle()
            if game_level==1:
                slide=5
                reset_sharknet()
            elif game_level==2:
                slide=9
                reset_oilbarrel()
            elif game_level==3:
                slide=13
                reset_trash()
            game_active = True
        if keyboard.escape:
            exit()
    if keyboard.space:
        if not game_active:
            if slide==4 or slide==8 or slide==12:
                game_active = True
                checkforactive()
            slide+=1
    if keyboard.escape:
        game_active = False
        SPEED=0
        count=0



def update_turtle():
    global game_active
    global count
    if game_level==1:
        if turtle.colliderect(shark1) or turtle.colliderect(shark2) or turtle.colliderect(net):
            turtle.dead=True
            turtle.image = 'player1dead'
            checkturtledead()
    elif game_level==2:
        if turtle.colliderect(oil1) or turtle.colliderect(oil2) or turtle.colliderect(barrel):
            turtle.dead=True
            turtle.image = 'turtletopdead'
            checkturtledead()
    elif game_level==3:
        if turtle.colliderect(trash1) or turtle.colliderect(trash2) or turtle.colliderect(trash3) or turtle.colliderect(trash4) or turtle.colliderect(trash5):
            turtle.dead=True
            turtle.image = 'player1dead'
            checkturtledead()
    if not 0 < turtle.top:
        turtle.top=1
    elif not turtle.bottom < HEIGHT:
        turtle.bottom=HEIGHT-1
    if not 0 < turtle.left:
        turtle.left=1
    elif not turtle.right < WIDTH:
        turtle.right=WIDTH-1


def reset_turtle():
    turtle.pos = (75, HEIGHT//2)
    turtle.image = 'player1'
    if game_level==2:
        turtle.image='turtletop'
    turtle.dead = False


def reset_shark1():
    shark1.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_shark2():
    shark2.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_net():
    net.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_sharknet():
    reset_shark1()
    reset_shark2()
    reset_net()
def update_sharknet():
    global count
    shark1.x -= SPEED+2
    shark2.x -= SPEED+1
    net.x -= SPEED-1
    if shark1.right < 0:
        reset_shark1()
        count+=1
        check_count()
    if shark2.right < 0:
        reset_shark2()
        count+=1
        check_count()
    if net.right < 0:
        reset_net()
        count+=1
        check_count()


def reset_oil1():
    oil1.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_oil2():
    oil2.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_barrel():
    oil2.pos = (WIDTH, random.randint(40,HEIGHT-40))
def reset_oilbarrel():
    reset_oil1()
    reset_oil2()
    reset_barrel()
def update_oilbarrel():
    global count
    oil1.x -= SPEED+2
    oil2.x -= SPEED+1
    barrel.x -= SPEED
    if oil1.right < 0:
        reset_oil1()
        count+=1
        check_count()
    if oil2.right < 0:
        reset_oil2()
        count+=1
        check_count()
    if barrel.right < 0:
        reset_barrel()
        count+=1
        check_count()


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
def reset_trash():
    reset_trash1()
    reset_trash2()
    reset_trash3()
    reset_trash4()
    reset_trash5()
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
        check_count()
    if trash3.right < 0:
        reset_trash3()
        count+=1
        check_count()
    if trash4.right < 0:
        reset_trash4()
        count+=1
        check_count()
    if trash5.right < 0:
        reset_trash5()
        count+=1
        check_count()




def update():
    global game_level
    update_turtle()
    checkturtledead()
    if game_level==1:
        update_sharknet()
    elif game_level==2:
        update_oilbarrel()
    elif game_level==3:
        update_trash()
    print(str(slide))