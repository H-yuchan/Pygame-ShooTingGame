
'''import pygame
pygame.init()
dis = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake game by JAMMIN')
blue = (0, 0, 255)
red = (255, 0, 0)
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pygame.draw.rect(dis, red, [0, 0, 200, 600])
    pygame.display.update()
pygame.quit()
quit()'''

'''
#사각형이 사각형 먹기
import pygame
import random
pygame.init()

white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
dis=pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake game by JAMMIN')

game_over = False

x = 300
y = 300
food_x=400
food_y=400
size=10
x_change =0
y_change =0
clock = pygame.time.Clock()
cnt=0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -10
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = 10
                x_change = 0
    dis.fill(black)
    x += x_change
    y += y_change
    if x<0:
        x=0
    elif x>600-size:
        x=600-size
    elif y>600-size:
        y=600-size
    elif y<0:
        y=0

    if food_x==x and food_y==y:
        food_x=random.randint(0,600-size)//10*10
        food_y = random.randint(0, 600 - size)
        cnt+=1
    if cnt==3:
        game_over = True

    pygame.draw.rect(dis, red, [x, y, size, size])
    pygame.draw.rect(dis, blue, [food_x, food_y, size, size])
    pygame.display.update()
    clock.tick(30)
pygame.quit()
quit()'''







'''#슈팅게임 프레임
import pygame
import sys
from time import sleep

BLACK = (0,0,0)
padWidth = 480
padHeight = 640

def initGame():
    global gamePad, clock
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock

    onGame =False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()
        gamePad.fill(BLACK)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
initGame()
runGame()'''


#전투기 배경삽입
'''import pygame
import sys
from time import sleep

BLACK = (0,0,0)
padWidth = 480
padHeight = 640

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, clock, background
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/background.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background

    onGame =False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()


        # gamePad.fill(BLACK)
        drawObject(background, 0, 0)
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
initGame()
runGame()
'''


#전투기 삽입
'''import pygame
import sys
from time import sleep

BLACK = (0,0,0)
padWidth = 480
padHeight = 640

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, clock, background, fighter
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/background.png')
    fighter = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/fighter.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x=padWidth * 0.45
    y=padHeight * 0.9
    fighterX = 0

    onGame =False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        drawObject(background, 0, 0)

        drawObject(fighter, x, y)
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
initGame()
runGame()
'''

#전투기 움직이기
'''import pygame
import sys
from time import sleep

BLACK = (0,0,0)
padWidth = 480
padHeight = 640

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, clock, background, fighter
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/background.png')
    fighter = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/fighter.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x=padWidth * 0.45
    y=padHeight * 0.9
    fighterX = 0

    onGame =False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -=5
                elif event.key == pygame.K_RIGHT:
                    fighterX +=5
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX =0

        drawObject(background, 0, 0)

        x+= fighterX
        if x< 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        drawObject(fighter, x, y)
        pygame.display.update()

        clock.tick(60)

    pygame.quit()
initGame()
runGame()
'''

#미사일 발사하기
'''import pygame
import sys
from time import sleep

BLACK = (0,0,0)
padWidth = 480
padHeight = 640

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, clock, background, fighter, missile
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/background.png')
    fighter = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/fighter.png')
    missile = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/missile.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter, missile

    missileXY = []

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x=padWidth * 0.45
    y=padHeight * 0.9
    fighterX = 0

    onGame =False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -=5
                elif event.key == pygame.K_RIGHT:
                    fighterX +=5
                elif event.key == pygame.K_SPACE:
                    missileX = x+fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX =0

        drawObject(background, 0, 0)

        x+= fighterX
        if x< 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        drawObject(fighter, x, y)

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -=10
                missileXY[i][1] = bxy[1]

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
initGame()
runGame()
'''

#랜덤 운석 떨어지기
'''import sys
import pygame
import random
from time import sleep
BLACK = (0,0,0)
padWidth = 480
padHeight = 640
rockImage = ['/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/rock01.png','/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/rock02.png']

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, clock, background, fighter, missile
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/background.png')
    fighter = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/fighter.png')
    missile = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/missile.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter, missile

    missileXY = []

    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]

    rockX = random.randrange(0,padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x=padWidth * 0.45
    y=padHeight * 0.9
    fighterX = 0

    onGame =False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -=5
                elif event.key == pygame.K_RIGHT:
                    fighterX +=5
                elif event.key == pygame.K_SPACE:
                    missileX = x+fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX =0

        drawObject(background, 0, 0)

        x+= fighterX
        if x< 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        drawObject(fighter, x, y)

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -=10
                missileXY[i][1] = bxy[1]

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        rockY +=rockSpeed

        if rockY > padHeight:
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]

            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
        drawObject(rock, rockX, rockY)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
initGame()
runGame()
'''


#운석 맞추기 미완성
'''import sys
import pygame
import random
from time import sleep
BLACK = (0,0,0)
padWidth = 480
padHeight = 640
rockImage = ['/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/rock01.png','/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/rock02.png']

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, clock, background, fighter, missile
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/background.png')
    fighter = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/fighter.png')
    missile = pygame.image.load('/Users/yuchan/PycharmProjects/pythonProject4/PyShooting/missile.png')
    explosion = pygame.image.load('PyShooting/explosion.png')
    clock = pygame.time.Clock()

def runGame():
    global gamePad, clock, background, fighter, missile


    isShot = False
    shotCount = 0
    rockPassed = 0

    missileXY = []

    rock = pygame.image.load(random.choice(rockImage))
    rockSize = rock.get_rect().size
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]

    rockX = random.randrange(0,padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2

    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]

    x=padWidth * 0.45
    y=padHeight * 0.9
    fighterX = 0

    onGame =False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT:
                    fighterX -=5
                elif event.key == pygame.K_RIGHT:
                    fighterX +=5
                elif event.key == pygame.K_SPACE:
                    missileX = x+fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX =0

        drawObject(background, 0, 0)

        x+= fighterX
        if x< 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        drawObject(fighter, x, y)

        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -=10
                missileXY[i][1] = bxy[1]

                if bxy[1] < rockY:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = T

                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)

        rockY +=rockSpeed

        if rockY > padHeight:
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]

            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
        drawObject(rock, rockX, rockY)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
initGame()
runGame()
'''