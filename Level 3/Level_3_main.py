import random

WIDTH = 1000
HEIGHT = 800
SPEED = 3
VELOCITY = 40
TARGET = 5

#functions
def presstoplay():
    screen.draw.text("Press space to play a game!", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
def presstocontinue():
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
    def __init__(self,game_level,live,dead,background,*enemies):
        self.game_level= game_level
        self.turtle=Actor(live,(75, HEIGHT//2) )
        self.turtle.dead=False
        self.turtle.x=75
        self.background=background
        self.enemies=[]
        for e in enemies:
            self.enemies.append(Actor(e, (WIDTH, (random.randint(0,HEIGHT))), anchor=('left', 'center')))
    def draw(self):
        screen.blit(self.background,(0,0))
        self.turtle.draw()
        for e in self.enemies:
            e.draw()
        screen.draw.text(count, midtop=(WIDTH-50, HEIGHT-100), color='white',fontsize=26)

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
slide11=slide('Ending text',None)

slides=[slide1,slide2,slide3,slide4,level1,slide5,slide6,slide7,level2,slide8,slide9,slide10,level3,slide11]


# Initial state of the turtle
i=0
count=0
#escape = False




def draw():
    global i
    slides[i].draw()
    print(i)

def check_count():
    global count
    global i
    if count >= TARGET:
        count = 0
        i+=1

def checkturtledead():
    global i
    global count
    if slides[i].turtle.dead:
        i=99
        count=0


def on_key_down():
    global i
    if i==4 or i==8 or i ==12:
        if not slides[i].turtle.dead:
            if keyboard.up:
                slides[i].turtle.y -= VELOCITY
            if keyboard.down:
                slides[i].turtle.y += VELOCITY
            if keyboard.left:
                slides[i].turtle.x -= VELOCITY
            if keyboard.right:
                slides[i].turtle.x += VELOCITY
  #  if slide == 99:
   #     if keyboard.space:
    #        reset_turtle()
     #       if game_level==1:
      #          slide=5
       #         reset_sharknet()
        #    elif game_level==2:
         #       slide=9
          #      reset_oilbarrel()
           # elif game_level==3:
            #    slide=13
             #   reset_trash()
         #   game_active = True
       # if keyboard.escape:
        #    exit()
    if keyboard.space:
        if not (i == 4 or i== 8 or i==12):
            i+=1
  #  if keyboard.escape:
   #     game_active = False
    #    SPEED=0
    #   count=0



def update_turtle():
    global count
    global slides
    if i==4:
        for e in slides[i].enemies:
            if slides[i].turtle.colliderect(e):
                slides[i].turtle.dead=True
                slides[i].turtle.image = 'player1dead'
                checkturtledead()
    elif i==8:
        for e in slides[i].enemies:
            if slides[i].turtle.colliderect(e):
                slides[i].turtle.dead=True
                slides[i].turtle.image = 'turtletopdead'
                checkturtledead()
    elif i==12:
       for e in slides[i].enemies:
            if slides[i].turtle.colliderect(e):
                slides[i].turtle.dead=True
                slides[i].turtle.image = 'player1dead'
                checkturtledead()

    if not 0 < slides[i].turtle.top:
        slides[i].turtle.top=1
    elif not slides[i].turtle.bottom < HEIGHT:
        slides[i].turtle.bottom=HEIGHT-1
    if not 0 < slides[i].turtle.left:
        slides[i].left=1
    elif not slides[i].turtle.right < WIDTH:
        slides[i].turtle.right=WIDTH-1


def reset_turtle():
    slides[i].turtle.pos = (75, HEIGHT//2)
    slides[i].turtle.image = 'player1'
    if i==4:
        slides[i].turtle.image='turtletop'
    slides[i].turtle.dead = False


def reset_enemy(enemy):
    enemy.pos = (WIDTH, random.randint(40,HEIGHT-40))
    #dV=random.randint(0,3)

def update_enemy(enemies):
    global count
    for e in enemies:
        e.x -= SPEED #+dV
    for e in enemies:
        if e.right < 0:
            reset_enemy(e)
            count+=1
            check_count()



def update():
    if i==4 or i==8 or i ==12:
        update_turtle()
        checkturtledead()
        update_enemy(slides[i].enemies)
    print(str(i))