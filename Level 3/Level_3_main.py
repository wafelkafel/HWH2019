import random
import numpy as np

WIDTH = 1000
HEIGHT = 800
SPEED = 3
VELOCITY = 40
TARGET = 5

#functions
def presstoplay():
    screen.draw.text("Press space to play", midtop=(WIDTH//2, HEIGHT//2), fontsize=32)
def presstocontinue():
    screen.draw.text("Press space to continue", midtop=(WIDTH//2, HEIGHT-100), fontsize=26)
def presstoexit():
    screen.draw.text("Press space to exit", midtop=(WIDTH//2, HEIGHT-100), fontsize=26)
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
        screen.draw.text(str(self.text), center=(WIDTH//2,HEIGHT//2), fontsize=32, width=600)
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
        screen.draw.text(str(count), color='white' , midtop=(WIDTH-50,HEIGHT-70),fontsize=60)

slide1=slide('Year 2005',presstocontinue)
slide2=slide('Toby is a sea turtle. He was 3 years old when something bad started happening. A coral reef that his species had lived in for thousands of years began to perish. He and his \
family had to find a new home. However, there were some dangers on the way.',presstocontinue)
slide3=slide('Sharks - turtles\' natural predators and shrimp nets used \
by humans were the greatest dangers that on Toby\'s way.',presstocontinue)
slide4=slide('',presstoplay)
level1=level(1,'player1','player1dead','coralreef','shark1','shark2','net')
slide5=slide('Year 2010',presstocontinue)
slide6=slide('The deepwater horizon oil spill in the Gulf of Mexico is considered the largest accidental marine oil spill in the history of the petroleum industry. The oil spill was a direct result \
of the explosion and sinking of the deepwater horizon oil rig. It killed thousands of marine mammals and sea turtles and contaminated their habitats.',presstocontinue)
slide7=slide('',presstoplay)
level2=level(2,'turtletop','turtletopdead','oceantop','oil1','oil2','barrel')
slide8=slide('Year 2019',presstocontinue)
slide9=slide('The Great Pacific Garbage Patch is the largest accumulation of ocean plastic in the world and is located between Hawaii and California. It covers an area three times the size of France. \
It poses great risks for the safety and health of marine animals. It consists mainly of plastics we use every day.',presstocontinue)
slide10=slide('',presstoplay)
level3=level(3,'player1','player1dead','ocean1','plasticbag','plasticbottle','sixpackrings','can','straw')
slide11=slide('However, there is still time to take action! If we act now, we can keep the oceans a good habitat for turtles and other animals to live in.',presstocontinue)
level4=level(4,'player1old',None,'coralreefhealthy','happyfish','happyoctopus','jellyfish','eel','crab')
slide12=slide('There are numerous organisations that decided to take up the challenge of cleaning up the oceans. \
Make sure you support them at:\n \n\
theoceancleanup.com\n\
plasticoceans.org\n\
4ocean.com\n\
5gyres.org\n\
oceana.org\n',presstoexit)
slide99=slide('', youlost)
slides=[slide1,slide2,slide3,slide4,level1,slide5,slide6,slide7,level2,slide8,slide9,slide10,level3,slide11, level4, slide12, slide99]


# Initial state of the turtle
i=0
count=0
temp=0

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
        count=0
        clock.schedule_unique((make99),1)
def make99():
    global i
    global temp
    temp=i
    i=len(slides)-1

def on_key_down():
    global i
    global count
    if i==4 or i==8 or i ==12 or i==14:
        if not slides[i].turtle.dead:
            if keyboard.up:
                slides[i].turtle.y -= VELOCITY
            if keyboard.down:
                slides[i].turtle.y += VELOCITY
            if keyboard.left:
                slides[i].turtle.x -= VELOCITY
            if keyboard.right:
                slides[i].turtle.x += VELOCITY
    elif i == len(slides)-1:
        if keyboard.space:
            i=temp
            count=0
            reset_turtle()
            for e in slides[i].enemies:
                e.x = WIDTH
        if keyboard.escape:
            exit()

    if keyboard.space:
        if not (i == 4 or i== 8 or i==12 or i==14):
            i+=1

def update_turtle():
    global count
    global slides
    if i==4 or i==12:
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



    if not 0 < slides[i].turtle.top:
        slides[i].turtle.top=1
    elif not slides[i].turtle.bottom < HEIGHT:
        slides[i].turtle.bottom=HEIGHT-1
    if not 0 < slides[i].turtle.left:
        slides[i].left=1
    elif not slides[i].turtle.right < WIDTH:
        slides[i].turtle.right=WIDTH-1


def reset_turtle():
    slides[i].turtle.dead = False
    slides[i].turtle.pos = (75, HEIGHT//2)
    slides[i].turtle.image = 'player1'
    if i==8:
        slides[i].turtle.image='turtletop'



def reset_enemy(enemy,x):
    ind = np.argmax(x)
    y0  = slides[i].enemies[ind].y
    delta = ((slides[i].enemies[ind].height)//2)+((enemy.height)//2)+(slides[i].turtle.height)
    if ((y0-delta)-20 > (HEIGHT-20-(y0+delta))):
        enemy.pos = (WIDTH, random.randint(20,y0 - delta-10))
    else:
        enemy.pos = (WIDTH, random.randint(y0+delta+10 ,HEIGHT-20))

def update_enemy(enemies):
    global count
    x=[0,0,0,0,0]
    for e in enemies:
        e.x -= SPEED+enemies.index(e)
        x[enemies.index(e)]=e.x
    for e in enemies:
        if e.right < 0:
            reset_enemy(e,x)
            count+=1
            check_count()


def update():
    if i==4 or i==8 or i ==12 or i==14:
        update_turtle()
        update_enemy(slides[i].enemies)

    print(str(i))