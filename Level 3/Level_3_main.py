import random

WIDTH = 1000
HEIGHT = 800
SPEED = 3
VELOCITY = 40
TARGET = 5



#functions
def presstoplay(slide):
    screen.draw.text("Press space to play a game!", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
def presstocontinue(slide):
    screen.draw.text("Press space to continue", midtop=(WIDTH//2, HEIGHT-100), fontsize=26)
def youlost():
    screen.draw.text("Sad fact", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
    screen.draw.text("Press space to try again or escape to exit the game", midtop=(WIDTH//2, HEIGHT-100), fontsize=26)

#objects/slides
class slide:
    def blackscreen(self):
        screen.fill((0,0,0))
    def __init__(self, text,prompt):
        self.text = text
        self.prompt=prompt
    def draw(self):
        self.blackscreen()
        screen.draw.text(str(self.text), midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
        self.prompt()

class level:
    def game_level(self, game_level):
        self.game_level= game_level

    def __init__(self,live,dead,background,*enemies):
        self.turtle=Actor(live,(75, HEIGHT//2) )
        self.background=background
        for e in enemies:
            self.enemies = self.enemies.append(Actor(e, (WIDTH, (random.randint(0,HEIGHT))), anchor=('left', 'center')))
    def draw(self):
        self.background.draw()
        self.turtle.draw()
        for e in self.enemies:
            e.draw()

slide1=slide('Year 2005',presstocontinue)
slide2=slide('First bunch of text',presstocontinue)
slide3=slide('Second bunch of text',presstocontinue)
slide4=slide('',presstoplay)
level1=level(1,'player1','player1dead','coralreef','shark1','shark2','net')
slide5=slide('Year 2010',presstocontinue)
slide6=slide('Third bunch of text',presstocontinue)
slide7=slide('',presstoplay)
level2=level(2,'turtletop','turtletopdead','oceantop','oil1','oil2','barrel')
slide8=slide('Year 2019',presstocontinue)
slide9=slide('Fourth bunch of text',presstocontinue)
slide10=slide('',presstoplay)
level3=level(3,'player1','player1dead','ocean1','plasticbag','plasticbottle','sixpackrings','can','straw')
slide11=slide('Ending text')

slides=[slide1,slide2,slide3,slide4,level1,slide5,slide6,slide7,level2,slide8,slide9,slide10,level3,slide11]


# Initial state of the turtle
turtle.dead = False
turtle.x = 75
count=0
game_active = False
game_level = 1
slide_count= 1
escape = False




def draw():
    slides[i].draw()
    print(i)

def check_count():
    global count
    global game_level
    global slide
    global game_active
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