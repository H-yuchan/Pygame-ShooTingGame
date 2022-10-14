#운석 맞추기 미완성
import sys
import pygame
import random
from time import sleep
BLACK = (0,0,0)
padWidth = 480
padHeight = 640
rockImage = ['PyShooting/rock01.png','PyShooting/rock02.png']

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj,(x,y))

def initGame():
    global gamePad, clock, background, fighter, missile, explosion
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')
    background = pygame.image.load('PyShooting/background.png')
    fighter = pygame.image.load('PyShooting/fighter.png')
    missile = pygame.image.load('PyShooting/missile.png')
    explosion = pygame.image.load('PyShooting/explosion.png')
    clock = pygame.time.Clock()


def writeScore(count):
    global gamePad
    font = pygame.font.Font('PyShooting/NanumGothic.ttf', 20)
    text = font.render('파괴한 운석 수:' + str(count), True, (255,255,255))
    gamePad.blit(text, (10,0))

def writePassde(count):
    global gamePad
    font = pygame.font.Font('PyShooting/NanumGothic.ttf', 20)
    text = font.render('놓친 운석 :' + str(count), True, (255, 0, 0))
    gamePad.blit(text, (360, 0))

#게임 메세지 출력
def writeMessge(text):
    global gamePad
    font = pygame.font.Font('PyShooting/NanumGothic.ttf', 80)
    text = font.render(text, True, (255, 0, 0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2, padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()

def crash():
    global gamePad
    writeMessge("전투기 파괴!")

def gameOver():
    global gamePad
    writeMessge("게임 오버!")

def runGame():
    global gamePad, clock, background, fighter, missile, explosion


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
    fighterY = 0
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
                elif event.key == pygame.K_UP:
                    fighterY -=5
                elif event.key == pygame.K_DOWN:
                    fighterY +=5
                elif event.key == pygame.K_SPACE:
                    missileX = x+fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX, missileY])
            if event.type in [pygame.KEYUP]:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX =0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighterY =0

        drawObject(background, 0, 0)

        x+= fighterX
        if x< 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth

        y+= fighterY
        if y<0:
            y=0
        elif y > padHeight - fighterWidth:
            y = padHeight - fighterWidth

        if y < rockY + rockHeight:
            if(rockX > x and rockX < x + fighterWidth) or (rockX + rockWidth > x and rockX + rockWidth< x + fighterWidth):
                crash()


        drawObject(fighter, x, y)

        if rockPassed ==3:#운석 3개 놓치면 게임 오버
            gameOver()


        if len(missileXY) != 0:
            for i, bxy in enumerate(missileXY):
                bxy[1] -=10
                missileXY[i][1] = bxy[1]

                if bxy[1] < rockY:
                    if bxy[0] > rockX and bxy[0] < rockX + rockWidth:
                        missileXY.remove(bxy)
                        isShot = True
                        shotCount += 1
                if bxy[1] <= 0:
                    try:
                        missileXY.remove(bxy)
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)


        writeScore(shotCount)

        rockY +=rockSpeed

        if rockY > padHeight:
            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]

            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            rockPassed +=1
        writePassde(rockPassed)
        if isShot:
            drawObject(explosion, rockX, rockY)

            rock = pygame.image.load(random.choice(rockImage))
            rockSize = rock.get_rect().size
            rockWidth = rockSize[0]
            rockHeight = rockSize[1]
            rockX = random.randrange(0, padWidth - rockWidth)
            rockY = 0
            isShot = False

            rockSpeed +=0.05
            if rockSpeed >= 10:
                rockSpeed =10



        drawObject(rock, rockX, rockY)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()
initGame()
runGame()