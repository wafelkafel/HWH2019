import random
import numpy as np
#display settings
WIDTH = 1000
HEIGHT = 800

#gameplay settings
SPEED = 4
VELOCITY = 40
TARGET = 1

# Initial state of the game
i=0
count=0
temp=0
action=0

#music
music.play('chameleon')

#functions for slides
def presstoplay1():
    screen.draw.text("Help Toby avoid obstacles\n\nUse arrow keys to navigate", center=(WIDTH//2, HEIGHT//2), fontsize=32)
    screen.draw.text("Press space to play", center=(WIDTH//2, HEIGHT-100), fontsize=26)
def presstoplay2():
    screen.draw.text("Toby doesn't have to avoid anything anymore!\n\nUse arrow keys to navigate\n", center=(WIDTH//2, HEIGHT//2), fontsize=32)
    screen.draw.text("Press space to play", center=(WIDTH//2, HEIGHT-100), fontsize=26)
def presstocontinue():
    screen.draw.text("Press space to continue", center=(WIDTH//2, HEIGHT-100), fontsize=26)
def presstoexit():
    screen.draw.text("Press space to exit", center=(WIDTH//2, HEIGHT-100), fontsize=26)
def youlost():
    fact()
    screen.draw.text("Press space to try again or escape to exit the game", center=(WIDTH//2, HEIGHT-100), fontsize=26)
def fact():
    facts=['100,000 marine mammals and turtles and 1 million sea  birds are killed by marine plastic pollution annually.',
    'Recent studies have revealed marine plastic pollution in 100% of marine turtles, 59% of whales, 36% of seals and 40% of seabird species examined.',
    'Over 150 plastic bottles litter each mile of UK beaches.',
    'Approx 5,000 items of marine plastic pollution have been found per mile of beach in the UK.',
    'Plastics consistently make up 60 to 90% of all marine debris studied.',
    'There may now be around 5.25 trillion macro and microplastic pieces floating in the open ocean. Weighing up to 269,000 tonnes.',
    'Every day approximately 8 million pieces of plastic pollution find their way into our oceans.',
    'Scientists have recently discovered microplastics embedded deep in the Arctic ice.',
    'Every minute, one garbage truck of plastic is dumped into our oceans.',
    'By 2050 there will be more plastic in the oceans than there are fish (by weight).',
    'There is more microplastic in the ocean than there are stars in the Milky Way.',
    'More than 50 percent of sea turtles have consumed plastic.']
    screen.fill((0,0,0))
    #a=random.randint(0,11)
    screen.draw.text(str(facts[action%(len(facts))]), center=(WIDTH//2, HEIGHT//2), fontsize=27, width=600, color='red')

#objects/slides
class slide:
    def blackscreen(self):
        screen.fill((0,0,0))
    def __init__(self,text,prompt):
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

#making slides and levels
slide1=slide('Year 2005',presstocontinue)
slide2=slide('Toby is a sea turtle. He was 3 years old when something bad started happening. \
A coral reef that his species had lived in for thousands of years began to perish. He and his \
family had to find a new home. However, there were some dangers on the way.',presstocontinue)
slide3=slide('Sharks - turtles\' natural predators and shrimp nets used \
by humans were the greatest dangers on Toby\'s way.',presstocontinue)
slide4=slide('',presstoplay1)
level1=level(1,'player1','player1dead','coralreef','shark1','shark2','net')
slide5=slide('Year 2010',presstocontinue)
slide6=slide('The deepwater horizon oil spill in the Gulf of Mexico is considered the largest accidental \
marine oil spill in the history of the petroleum industry. The oil spill was a direct result \
of the explosion and sinking of the deepwater horizon oil rig. It killed thousands of marine mammals \
and sea turtles and contaminated their habitats.',presstocontinue)
slide7=slide('',presstoplay1)
level2=level(2,'turtletop','turtletopdead','oceantop','oil1','oil2','barrel')
slide8=slide('Year 2019',presstocontinue)
slide9=slide('The Great Pacific Garbage Patch is the largest accumulation of ocean plastic in the world \
and is located between Hawaii and California. It covers an area three times the size of France. \
It poses great risks for the safety and health of marine animals. It consists mainly of plastics we use every day.',presstocontinue)
slide10=slide('',presstoplay1)
level3=level(3,'player1','player1dead','ocean1','plasticbag','plasticbottle','sixpackrings','can','straw')
slide11=slide('However, there is still time to take action! If we act now, we can keep the oceans \
a good habitat for turtles and other animals to live in.',presstocontinue)
slide12=slide('If we take action, this is what the oceans could look like',presstocontinue)
slide13=slide('Year 2100',presstocontinue)
slide14=slide('',presstoplay2)
level4=level(4,'player1old',None,'coralreefhealthy','happyfish','happyoctopus','jellyfish','eel','crab')
slide15=slide('There are numerous organisations that decided to take up the challenge of cleaning up the oceans.\
 Make sure you support them at:\n\n\
theoceancleanup.com\n\
plasticoceans.org\n\
4ocean.com\n\
5gyres.org\n\
oceana.org\n',presstoexit)
slide99=slide('', youlost)

#combine slides
slides=[slide1,slide2,slide3,slide4,level1,slide5,slide6,slide7,level2,slide8,slide9,slide10,level3,slide11, slide12,slide13,slide14,level4, slide15, slide99]

def draw():
    slides[i].draw()

#define what happens for pressing different keys
def on_key_down():
    global i
    global count
    global action
    if i==4 or i==8 or i ==12 or i==17:
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
            reset_turtle()
            for e in slides[i].enemies:
                e.x = WIDTH
        if keyboard.escape:
            music.stop()
            exit()

    if keyboard.space:
        if not (i == 4 or i== 8 or i==12 or i==17 or i==18):
            i+=1
        elif i==18:
            music.top()
            exit()
    action+=1

#update turtle info
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
        slides[i].turtle.left=1
    elif not slides[i].turtle.right < WIDTH:
        slides[i].turtle.right=WIDTH-1

#cchecking the count in game
def check_count():
    global count
    global i
    if count >= TARGET:
        count = 0
        i+=1

#see if tutrtle died
def checkturtledead():
    global count
    if slides[i].turtle.dead:
        clock.schedule_unique((make99),1)

#go to slide with sad fact
def make99():
    global i
    global temp
    temp=i
    i=len(slides)-1

#reset turtle position and state
def reset_turtle():
    count=0
    slides[i].turtle.dead = False
    slides[i].turtle.pos = (75, HEIGHT//2)
    slides[i].turtle.image = 'player1'
    if i==8:
        slides[i].turtle.image='turtletop'


#update enemy's position
def update_enemy(enemies):
    global count
    x=[0,0,0,0,0]
    for e in enemies:
        e.x -= SPEED+enemies.index(e)
        x[enemies.index(e)]=e.right
    for e in enemies:
        if e.right < 0:
            reset_enemy(e,x)
            count+=1
            check_count()

#reset enemy's position
def reset_enemy(enemy,x):
    ind = np.argmax(x)
    y0  = slides[i].enemies[ind].y
    delta = ((slides[i].enemies[ind].height)//2)+((enemy.height)//2)+(slides[i].turtle.height)
    if ((y0-delta)-20 > (HEIGHT-20-(y0+delta))):
        enemy.pos = (WIDTH, random.randint(20,y0 - delta-10))
    else:
        enemy.pos = (WIDTH, random.randint(y0+delta+10 ,HEIGHT-20))

def update():
    if i==4 or i==8 or i ==12 or i==17:
        update_turtle()
        update_enemy(slides[i].enemies)