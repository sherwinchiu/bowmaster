#################################################
# finalgame.py                                  #
# Sherwin Chiu                                  #
# 12/13/2017                                    #
# Final assignment for comp sci                 #
#################################################
#----------------------#
# Imports              #
#----------------------#
import pygame
pygame.init()
from random import randint
import time
#Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
#----------------------#
# Pictures             #
#----------------------#
    
#Player 
Player = [0] * 5

PlayerShootLeft = [0] * 11
PlayerShootRight = [0] * 11
for i in range(4):
    Player[i] = pygame.image.load("Player/player" + str(i) +".png").convert_alpha()
for i in range(11):
    PlayerShootLeft[i] = pygame.image.load("Player/Player Shoot Left/playershoot" + str(i) + ".png").convert_alpha()
    PlayerShootRight[i] = pygame.image.load("Player/Player Shoot Right/playershoot" + str(i)+ ".png").convert_alpha()
#Stages
mainMenu = [0] * 2
background = [0] * 4
mainFloor = [0] * 7
mainFloorAnimate = 0
mainMenuCounter = 0
showmainMenu = True
for i in range (2):
    mainMenu[i] = pygame.image.load("Background/mainmenu"+str(i)+".png").convert()
for i in range (4):
    background[i] = pygame.image.load("Background/background"+str(i)+".png").convert()
for i in range(7):
    mainFloor[i] = pygame.image.load("Background/mainFloor"+str(i) +".png").convert()

    
#Arrow
Arrow = [0] * 2

Rope = pygame.image.load("Misc/Arrow/Rope.png").convert_alpha()
Anchor = pygame.image.load("Misc/Arrow/Anchor.png").convert_alpha()
for i in range(2):
    Arrow[i] = pygame.image.load("Misc/Arrow/Arrow " + str(i) +".png").convert_alpha()
  
    
enemyArrow = Arrow


#Platforms
platform = [0]
for i in range(1):
    platform[i] = pygame.image.load("Background/platform"+str(i) + ".png").convert()
#Enemies
enemyNorm = [0] * 3
enemyBow = [0] * 4
enemyFly = [0] * 2
for i in range(2):
    enemyFly[i] = pygame.image.load("Enemies/Flying Enemy/flyenemy"+str(i) + ".png").convert_alpha()
for i in range(3):
    enemyNorm[i] = pygame.image.load("Enemies/Enemy/normenemy"+str(i) + ".png").convert_alpha()
for i in range(4):
    enemyBow[i] = pygame.image.load("Enemies/Bow Enemy/bowenemy"+str(i) + ".png").convert_alpha()
#Hearts
heart = [0] * 2
for i in range(2):
    heart[i] = pygame.image.load("Misc/Full Heart/heart"+str(i) + ".png").convert_alpha()
#Door
door = [0] * 3
for i in range(3):
    door[i] = pygame.image.load("Misc/Door/door"+str(i) +".png").convert_alpha()
#----------------------#
# Variables            #
#----------------------#
#Constants
GRAVITY = 2
GROUND = 582
BEGIN = time.time()
LEFTWALL = 22
RIGHTWALL = 770
ARROWSTEP = 15
BLACK = (0,0,0)
#Player
playerX = 40
playerY = 500
playerRect = Player[0].get_rect()
playerHeight = playerRect.height 
playerWidth = playerRect.width - 20
playerRect1 = pygame.Rect(playerX, playerY, playerHeight,playerWidth)
speedX = 7
speedY = -22
velocityY = 0
directionPlayer = "Right"
runAnimation = False
runAnimate = 0
immortalityCounter = 0
runCounter = 2
#Arrow
arrowX = [ ] 
arrowY = [ ] 
arrowRect = [Arrow[0].get_rect()]
arrowWidth = arrowRect[0].width
arrowHeight = arrowRect[0].height
arrowVis = [ ] 
arrowDir= [ ] 
arrowSpeed = [ ] 
arrowCounter = 0
arrowAnimation = False
arrowAnimate = 0
maxArrows = 3
drawArrow = False
drawRope = False
drawAnchor = False
#Rope on Arrow
anchorX = [ ]
anchorY = [ ]
ropeX = [ ]
ropeY = [ ]
ropeRect = [Rope.get_rect()]
ropeWidth = ropeRect[0].width
ropeHeight = 8
ropeCounter = 0
ropeAmount = 0
#Platforms
platformX = [ ]
platformY = [ ]
platformRectTop = [ ]
platformRectBottom = [ ]
platformRectLeft = [ ]
platformRectRight = [ ]
hitBoxWidth = 5
numberOfPlatforms = 5
platformPlacement = 550
#Enemies
enemyFlyX = [ ]
enemyFlyY = [ ]
enemyBowX = [ ]
enemyBowY = [ ]
#Enemy Arrows
enemyArrowX = [ ]
enemyArrowY = [ ]
enemyArrowRect = [enemyArrow[0].get_rect()]
enemyArrowWidth = enemyArrowRect[0].width
enemyArrowHeight = enemyArrowRect[0].height
enemyArrowVis = [ ] 
enemyArrowDir = [ ] 
enemyArrowSpeed = [ ]
enemyArrowDisappear = 0

enemyNormX = [ ]
enemyNormY = [ ]
enemyFlyRect = [ ]
enemyBowRect = [ ]
enemyNormRect = [ ]

enemyWidth = 60
enemyHeight = 36

numberOfFly = randint(1,3)
numberOfBow = randint(1,3)
numberOfNorm = randint(1,3)
lowBarrierFly = [ ] 
highBarrierFly = [ ] 
leftNormBarrier = [ ]
rightNormBarrier = [ ]
enemyStep = 1
#Hearts
heartX = [ ]
heartY = 30
heartWidth = 33
heartHeight = 30
heartCounter = [ ]
heartPlacement = 650
for i in range(3):
    heartX.append(heartPlacement)
    heartPlacement = heartPlacement + heartWidth
    heartCounter.append(True)
heartNumber = 2
#Door
doorRect = door[0].get_rect()
doorWidth = doorRect.width/2
doorHeight = doorRect.height
doorX = [ ]
doorY = [ ]
doorCounter = 0
doorOpen = False
#Main menu button hit boxes
playRect = pygame.Rect(275,213,215,88)
controlRect = pygame.Rect(252,322,245,88)
quitRect = pygame.Rect(278,450,175,82)
backRect= pygame.Rect(600,0,175,100)
#Fonts
font = pygame.font.SysFont("Arial", 54)
#Reseting stage
nextStage = False
lastLevel = False
stageCounter = -1
#----------------------#
# Functions            #
#----------------------#
def redrawScreen(mainFloorAnimate):
    if showmainMenu == True:
        screen.blit(mainMenu[mainMenuCounter],(0,0))
    elif stageCounter == 0:
        screen.blit(mainFloor[int(round(mainFloorAnimate,1))],(0,0))
    else:
        screen.blit(background[stageCounter-1],(0,0))
    if showmainMenu != True:
        drawPlayer()
        drawHearts()
        drawArrows()
        drawRopes()
        if stageCounter < 4:
            drawEnemyArrows()
            drawPlatforms()
            drawDoor()
            drawEnemies()
            drawEndScreen()
        if stageCounter == 4:
            drawEndScreen()
    pygame.display.update()
def drawPlatforms():
    for i in range(numberOfPlatforms):
        screen.blit(platform[0],(platformX[i],platformY[i]))
def drawPlayer():
    # Draw player 2 standing
    if directionPlayer == "Left" and arrowAnimation == False and runAnimation == False:
        screen.blit(Player[int(round(runCounter,1))],(playerX,playerY))
    if directionPlayer == "Right" and arrowAnimation == False and runAnimation == False:
        screen.blit(Player[int(round(runCounter,1))],(playerX + 20,playerY)) 
    # Running animation
    if directionPlayer == "Left" and runAnimation == True:
        screen.blit(P2RunLeft[int(round(runAnimate,1))],(playerX,playerY))
    if directionPlayer == "Right" and runAnimation == True:
        screen.blit(P2RunRight[int(round(runAnimate,1))],(playerX,playerY))    
    #Arrow animation 
    if directionPlayer == "Left" and arrowAnimation == True:
        screen.blit(PlayerShootLeft[int(arrowAnimate)],(playerX,playerY))
    if directionPlayer == "Right" and arrowAnimation == True:
        screen.blit(PlayerShootRight[int(arrowAnimate)],(playerX + playerWidth /2,playerY))
    
def drawArrows():
    for i in range(len(arrowX)):
        if arrowVis[i] and arrowDir[i] == "Left":
            screen.blit(Arrow[0],(arrowX[i],arrowY[i] + playerHeight/2))
        if arrowVis[i] and arrowDir[i] == "Right":    
            screen.blit(Arrow[1],(arrowX[i] - 45,arrowY[i] + playerHeight/2))
def drawEnemyArrows():
    for i in range(len(enemyArrowX)):
        if enemyArrowVis[i] and enemyArrowDir[i] == "Left":
            screen.blit(enemyArrow[1],(enemyArrowX[i],enemyArrowY[i] + enemyHeight/2))
        if enemyArrowVis[i] and enemyArrowDir[i] == "Right":
            screen.blit(enemyArrow[0],(enemyArrowX[i],enemyArrowY[i] + enemyHeight/2))   
def drawRopes():
    for i in range(len(anchorX)):
        screen.blit(Anchor,(anchorX[i],anchorY[i] + playerHeight/2))
    for i in range(len(ropeX)):
        screen.blit(Rope,(ropeX[i],ropeY[i] + playerHeight/2))


def drawEnemies():
    for i in range(numberOfFly):
        if enemyFlyVis[i] and enemyDirFly[i] == "Up":
            screen.blit(enemyFly[0],(enemyFlyX[i],enemyFlyY[i]))
        if enemyFlyVis[i] and enemyDirFly[i] == "Down":
            screen.blit(enemyFly[1],(enemyFlyX[i],enemyFlyY[i]))
            
    for i in range(numberOfBow):
        if enemyBowVis[i] and enemyDirBow[i] == "Left":
            screen.blit(enemyBow[0],(enemyBowX[i],enemyBowY[i]))
        if enemyBowVis[i] and enemyDirBow[i] == "Right":
            screen.blit(enemyBow[2],(enemyBowX[i],enemyBowY[i]))
            
    for i in range(numberOfNorm):
        if enemyNormVis[i]:
            screen.blit(enemyNorm[0],(enemyNormX[i],enemyNormY[i]))
        
def drawHearts():
    for i in range(len(heartX)):
        if heartCounter[i]:
            screen.blit(heart[0], (heartX[i],heartY))
        else:
            screen.blit(heart[1], (heartX[i],heartY))
def drawDoor():
    screen.blit(door[doorCounter],(doorX,doorY))
def drawEndScreen():
    if heartNumber <= -1:
        print "You Lose!"
        screen.fill(BLACK)
    if stageCounter == 4:
        screen.blit(playTime,(250,40))
        screen.blit(ropeUses,(285,140))
def removeArrow(i):
    arrowX.pop(i)
    arrowY.pop(i)
    arrowDir.pop(i)
    arrowSpeed.pop(i)
    arrowVis.pop(i)
    arrowRect.pop(i)
    arrowSpeed.append(ARROWSTEP)
    arrowVis.append(True)
def removeEnemyArrow(i):
    enemyArrowX.pop(i)
    enemyArrowY.pop(i)
    enemyArrowDir.pop(i)
    enemyArrowSpeed.pop(i)
    enemyArrowVis.pop(i)
    enemyArrowRect.pop(i)
def removeRope():
    drawRope = False
    for i in range(len(ropeX)):
        ropeX.pop(0)
        ropeY.pop(0)
        ropeRect.pop(0)
    for i in range(len(anchorX)-1):
        anchorX.pop(0)
        anchorY.pop(0)
def removeFly(i):
    enemyFlyX.pop(i)
    enemyFlyY.pop(i)
    enemyFlyRect.pop(i)
    highBarrierFly.pop(i)
    lowBarrierFly.pop(i)
def removeBow(i):
    enemyBowX.pop(i)
    enemyBowY.pop(i)
    enemyBowRect.pop(i)
def removeNorm(i):
    enemyNormX.pop(i)
    enemyNormY.pop(i)
    enemyNormRect.pop(i)
    leftNormBarrier.pop(i)
    rightNormBarrier.pop(i)
#----------------------#
# Main Program         #
#----------------------#
inPlay = True
clock = pygame.time.Clock()
FPS = 60
while showmainMenu:
    redrawScreen(mainFloorAnimate)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouseX,mouseY) = pygame.mouse.get_pos()
            mouse = pygame.Rect(mouseX,mouseY,5,5)
            if mouse.colliderect(playRect) and mainMenuCounter == 0:
                showmainMenu = False
            if mouse.colliderect(controlRect):
                mainMenuCounter = 1
            if mouse.colliderect(backRect) and mainMenuCounter == 1:
                mainMenuCounter = 0
                
            if mouse.colliderect(quitRect) and mainMenuCounter == 0:
                showmainMenu = False
                inPlay = False
            clock.tick(FPS)
while inPlay:
    #Reset variables every
    immortalityCounter = immortalityCounter + 1
    for i in range(len(enemyBowX)):
        enemyArrowCounter[i] = enemyArrowCounter[i] + 1
    #Start a new stage
    if nextStage == False:
    #Remove things from last stage and reset

        if enemyFlyX != []:
            for i in range(len(arrowX)):
                removeArrow(0)
            removeRope()
            for i in range(numberOfFly):
                removeFly(0)
            for i in range(numberOfBow):
                removeBow(0)
            for i in range(numberOfNorm):
                removeNorm(0)
            platformPlacement = 550
            for i in range(numberOfPlatforms):
                platformX.pop(0)
                platformY.pop(0)
                platformRectTop.pop(0)
                platformRectBottom.pop(0)
                platformRectLeft.pop(0)
                platformRectRight.pop(0)
        playerX = 40
        playerY = 500
        for i in range(numberOfPlatforms):
            platformX.append(randint(50,650))
            platformY.append(platformPlacement)
            platformPlacement = platformPlacement - 150
            platformRectTop.append(platform[0].get_rect())
            platformRectBottom.append(platform[0].get_rect())
            platformRectLeft.append(platform[0].get_rect())
            platformRectRight.append(platform[0].get_rect())
        platformWidth = platformRectTop[0].width
        platformHeight = platformRectTop[0].height
        doorRect = door[0].get_rect()
        doorWidth = doorRect.width/2
        doorHeight = doorRect.height
        doorX = platformX[3] + 15
        doorY = platformY[3] - doorHeight + 5
        doorCounter = 0
        doorOpen = False
        numberOfFly = randint(1,3)
        numberOfBow = randint(1,3)
        numberOfNorm = randint(1,3)
        enemyDirFly = ["Up"] * numberOfFly
        enemyDirBow = ["Left"] * numberOfBow
        enemyDirNorm = ["Left"] * numberOfNorm
        enemyFlyVis = [True] * numberOfFly
        enemyBowVis = [True] * numberOfBow
        enemyNormVis = [True] * numberOfNorm
        enemyArrowCounter = [0] * numberOfBow
        enemyDeathCounter = 0
        numberOfEnemies = numberOfFly + numberOfBow + numberOfNorm
        for i in range(numberOfFly):
            enemyFlyX.append(randint(100,650))
            enemyFlyY.append(randint(50,500))
            enemyFlyRect.append(enemyFly[0].get_rect())                
            highBarrierFly.append(enemyFlyY[i] - 100)
            lowBarrierFly.append(enemyFlyY[i] + 100)
    
        for i in range(numberOfBow):
            enemyBowX.append(randint(100,700))
            enemyBowY.append(randint(100,550))
            enemyBowRect.append(enemyBow[0].get_rect())
        for i in range(numberOfNorm):
            enemyNormX.append(randint(200,600))
            enemyNormY.append(randint(100,550))
            enemyNormRect.append(enemyNorm[0].get_rect())
            leftNormBarrier.append(enemyNormX[i] - 100)
            rightNormBarrier.append(enemyNormX[i] + 100)
        stageCounter = stageCounter + 1
        nextStage = True

    #Reset hit boxes
    if directionPlayer == "Right":
        playerRect1 = pygame.Rect(playerX + 19, playerY, playerWidth + 3,playerHeight)
    if directionPlayer == "Left":
        playerRect1 = pygame.Rect(playerX+ 18, playerY, playerWidth + 3, playerHeight)
    for i in range(len(arrowX)):
        if arrowDir[i] == "Right":
            arrowRect[i] = pygame.Rect(arrowX[i] - arrowWidth * 1.5,arrowY[i] + 40,arrowWidth,arrowHeight)
        if arrowDir[i] == "Left":
            arrowRect[i] = pygame.Rect(arrowX[i],arrowY[i] + 40,arrowWidth,arrowHeight)
    for i in range(len(enemyArrowX)):
        enemyArrowRect[i] = pygame.Rect(enemyArrowX[i], enemyArrowY[i] +18,enemyArrowWidth,enemyArrowHeight)
    for i in range(len(ropeX)):
        ropeRect[i] = pygame.Rect(ropeX[i], ropeY[i] +40, ropeWidth, ropeHeight)
    for i in range(numberOfPlatforms):
        platformRectTop[i] = pygame.Rect(platformX[i] + 10, platformY[i],platformWidth - 20,hitBoxWidth)
        platformRectBottom[i] = pygame.Rect(platformX[i] + 10, platformY[i] + platformHeight - 5,platformWidth - 20,hitBoxWidth)
        platformRectLeft[i] = pygame.Rect(platformX[i], platformY[i] + hitBoxWidth,hitBoxWidth*10,platformHeight - 10)
        platformRectRight[i] = pygame.Rect(platformX[i] + platformWidth -  hitBoxWidth*10, platformY[i] + hitBoxWidth ,hitBoxWidth *10,platformHeight - 10)
    for i in range(numberOfFly):
        enemyFlyRect[i] = pygame.Rect(enemyFlyX[i], enemyFlyY[i], enemyWidth + 40,enemyHeight)
    for i in range(numberOfBow):
        enemyBowRect[i] = pygame.Rect(enemyBowX[i], enemyBowY[i], enemyWidth + 15,enemyHeight)
    for i in range(numberOfNorm):
        enemyNormRect[i] = pygame.Rect(enemyNormX[i], enemyNormY[i], enemyWidth, enemyHeight)
    doorRect = pygame.Rect(doorX,doorY,doorWidth,doorHeight)
#Reset animation
    if stageCounter < 4:
        elapsedTime = round(time.time() - BEGIN,2)
    ropeUses = font.render(str(ropeAmount), 1,BLACK)
    playTime = font.render(str(elapsedTime), 1,BLACK)
    redrawScreen(mainFloorAnimate)
    #Animations
    mainFloorAnimate = mainFloorAnimate + 0.2
    if mainFloorAnimate >= len(mainFloor):
        mainFloorAnimate = 0
    if runAnimation == True:
        runAnimate = runAnimate + 0.2
        if runAnimate >= len(P2RunLeft):
            runAnimate = 0
    if runAnimation == False:
        runAnimate = 0  
    if arrowAnimation == True:
        arrowAnimate = arrowAnimate + 0.5
        if arrowAnimate >= 11:
            arrowAnimate = 0
            arrowAnimation = False
    if round(runCounter) == 3:
        runCounter = 2
    if round(runCounter) == 0:
        runCounter = 1    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        inPlay = False
#Player controls
    if keys[pygame.K_UP] and playerY + playerHeight == GROUND:
        velocityY = speedY
    if keys[pygame.K_LEFT] and playerX >= LEFTWALL - playerWidth/2:
        playerX = playerX - speedX
        directionPlayer = "Left"
        runCounter = runCounter - 0.5
    if keys[pygame.K_RIGHT] and playerX + playerWidth * 1.33 <= RIGHTWALL:
        playerX = playerX + speedX
        directionPlayer = "Right"
        runCounter = runCounter + 0.5
    clock.tick(FPS)
    #Limit arrows shot
    arrowCounter = arrowCounter + 0.05
    #shoot arrows
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o  and arrowCounter >= 2:
                arrowAnimation = True
                arrowCounter = 0
                drawRope = True
                drawAnchor = True
                drawArrow = False
                ropeAmount = ropeAmount + 1

            if event.key == pygame.K_p  and arrowCounter >= 2:
                arrowCounter = 0
                arrowAnimation = True
                drawArrow = True
                drawRope = False
                drawAnchor = False
    if arrowAnimate == 9:        
        if directionPlayer == "Left":
            arrowX.append(playerX + playerHeight/2 - 60)
        if directionPlayer == "Right":
            arrowX.append(playerX + playerHeight/2 + 60)
        arrowY.append(playerY)
        arrowDir.append(directionPlayer)
        arrowSpeed.append(ARROWSTEP)
        arrowVis.append(True)
        for i in range(len(arrowX)):
            arrowRect.append(pygame.Rect(arrowX[i],arrowY[i],arrowWidth,arrowHeight))
        if drawAnchor == True and drawArrow == False:
            if directionPlayer == "Left":
                anchorX.append(playerX + playerHeight/2 - 30)
            if directionPlayer == "Right":
                anchorX.append(playerX + playerHeight/2 + 30)
            anchorY.append(playerY)
            drawAnchor = False
    pygame.event.get()
# move and decay the arrow
    numArrow = len(arrowX)
    for i in range(len(enemyArrowX)):
        if enemyArrowDir[i] == "Right":
            enemyArrowX[i] = enemyArrowX[i] - enemyArrowSpeed[i]
        if enemyArrowDir[i] == "Left":
            enemyArrowX[i] = enemyArrowX[i] + enemyArrowSpeed[i]
    for i in range(numArrow):
        if arrowDir[i] == "Left":
            arrowX[i] = arrowX[i] - arrowSpeed[i]
        if arrowDir[i] == "Right":
            arrowX[i] = arrowX[i] + arrowSpeed[i]
        if arrowSpeed[i] == ARROWSTEP and drawRope == True and drawArrow == False:
            if arrowDir[i] == "Left":
                ropeX.append(arrowX[i] + 40)
            if arrowDir[i] == "Right":
                ropeX.append(arrowX[i] - 55)
            ropeY.append(arrowY[i] + 2)
            for rope in range(len(ropeX)):
                ropeRect.append(pygame.Rect(ropeX[rope], ropeY[rope] +40, ropeWidth, ropeHeight))
        if arrowX[i] >= RIGHTWALL or arrowX[i] <= LEFTWALL:
            arrowSpeed[i] = 0
# Allow arrows to be visible
        if arrowX[i] >= RIGHTWALL:
            arrowX[i] = RIGHTWALL + arrowWidth/1.5
        if arrowX[i] <= LEFTWALL:
            arrowX[i] = LEFTWALL 
# Remove arrows if there are more than 6 arrows
    for i in range(len(arrowX)):
        if len(arrowX) >= maxArrows:
            removeArrow(0)
            removeRope()
            arrowSpeed[i] = 20
# arrow hit boxes
    for i in range(len(arrowX)):
        #arrowhit box for jumping on
        if arrowRect[i].colliderect(playerRect1) and playerY + playerHeight >= arrowY[i] and velocityY > 0:
            playerY = arrowY[i] - playerHeight/2 + GRAVITY
            velocityY = 0
            if keys[pygame.K_UP]:
                velocityY = speedY
    for i in range(len(ropeX)):
        if ropeRect[i].colliderect(playerRect1) and playerY + playerHeight >= ropeY[i] and velocityY >0:
            for arrow in range(len(arrowX)):
                playerY = ropeY[i] - playerHeight/2 + GRAVITY
                velocityY = 0
                if keys[pygame.K_UP]:
                    velocityY = speedY
    velocityY = velocityY + GRAVITY
    playerY = playerY + velocityY
    if playerY + playerHeight >= GROUND:
        playerY = GROUND - playerHeight
        velocityY = 0

# Platform hit box

    if stageCounter !=4:
        for i in range(numberOfPlatforms):
            #Hit box for player
            if platformRectTop[i].colliderect(playerRect1) and velocityY > -1:
                playerY = platformY[i] - playerHeight + GRAVITY 
                velocityY = 0
                if keys[pygame.K_UP]:
                    velocityY = speedY
            if platformRectBottom[i].colliderect(playerRect1) and playerY <= platformY[i] + platformHeight:
                velocityY = 0
                playerY = platformY[i] + platformHeight
            if platformRectLeft[i].colliderect(playerRect1) and not platformRectTop[i].colliderect(playerRect1) and not platformRectBottom[i].colliderect(playerRect1) and directionPlayer == "Right":
                playerX = platformX[i] - playerWidth - 20
            if platformRectRight[i].colliderect(playerRect1) and not platformRectTop[i].colliderect(playerRect1) and not platformRectBottom[i].colliderect(playerRect1) and directionPlayer == "Left": 
                playerX = platformX[i] + platformWidth - 20
            for rope in range(len(ropeX)):
                if ropeRect[rope].colliderect(playerRect1) and platformRectBottom[i].colliderect(playerRect1):
                    playerY = ropeY[i] + playerHeight
                    
                    
                    
            #hit box for arrows with platforms                              
            for arrow in range(len(arrowX)):
                if arrowRect[arrow].colliderect(platformRectRight[i]) and arrowDir[arrow] == "Left":
                    arrowSpeed[arrow] = 0
                    arrowX[arrow] = platformX[i] + platformWidth 
                if arrowRect[arrow].colliderect(platformRectLeft[i]) and arrowDir[arrow] == "Right":
                    arrowSpeed[arrow] = 0
                    arrowX[arrow] = platformX[i] + arrowWidth/2
#Enemy physics
#Bow
        for bow in range(numberOfBow):
            enemyBowY[bow] = enemyBowY[bow] + GRAVITY
            if enemyBowY[bow] + enemyHeight >= GROUND:
                enemyBowY[bow] = GROUND - enemyHeight
            if playerX >= enemyBowX[bow]:
                enemyDirBow[bow] = "Left"
            else:
                enemyDirBow[bow] = "Right"
            for i in range(numberOfPlatforms):
                if enemyBowRect[bow].colliderect(platformRectTop[i]):
                    enemyBowY[bow] = platformY[i] - enemyHeight + 1
            if enemyArrowCounter[bow] >= 200 and enemyBowVis[bow]:
                if enemyDirBow[bow] == "Left":
                    enemyArrowX.append(enemyBowX[bow] + enemyHeight/2)
                if enemyDirBow[bow] == "Right":
                    enemyArrowX.append(enemyBowX[bow] + enemyHeight/2)
                enemyArrowY.append(enemyBowY[bow])
                enemyArrowDir.append(enemyDirBow[bow])
                enemyArrowSpeed.append(15)
                enemyArrowVis.append(True)
                enemyArrowCounter[bow] = 0
                
            for i in range(len(enemyArrowX)):
                enemyArrowRect.append(enemyArrow[0].get_rect())
                if enemyArrowRect[i].colliderect(playerRect1) and immortalityCounter >= 45:
                    heartCounter.pop(heartNumber)
                    heartCounter.append(False)
                    heartNumber = heartNumber - 1
                    immortalityCounter = 0
                    removeEnemyArrow(i)
            for i in range(len(enemyArrowX)-1):
                if not enemyArrowRect[i].colliderect(playerRect1) and enemyArrowX[i] <= LEFTWALL - enemyArrowWidth:
                    removeEnemyArrow(i)
                if not enemyArrowRect[i].colliderect(playerRect1) and enemyArrowX[i] >= RIGHTWALL + enemyArrowWidth:
                    removeEnemyArrow(i)
                    
            if enemyBowRect[bow].colliderect(playerRect1) and enemyBowVis[bow] != False and immortalityCounter >= 45:
                heartCounter.pop(heartNumber)
                heartCounter.append(False)
                heartNumber = heartNumber - 1
                immortalityCounter = 0
            for arrow in range(len(arrowX)):
                if arrowRect[arrow].colliderect(enemyBowRect[bow]) and arrowSpeed[arrow] == ARROWSTEP and drawArrow == True and enemyBowVis[bow] != False:
                    enemyBowVis[bow] = False
                    removeArrow(arrow)
                    removeRope()
                    enemyDeathCounter = enemyDeathCounter + 1
    #Normal 
        for norm in range(numberOfNorm):
            enemyNormY[norm] = enemyNormY[norm] + GRAVITY
            if enemyNormY[norm] + enemyHeight >= GROUND:
                enemyNormY[norm] = GROUND - enemyHeight         
            for i in range(numberOfPlatforms):
                if enemyNormRect[norm].colliderect(platformRectTop[i]):
                    enemyNormY[norm] = platformY[i] - enemyHeight + GRAVITY
            enemyNormX[norm] = enemyNormX[norm] + enemyStep
            if enemyNormX[norm] <= rightNormBarrier[norm]:
                enemyStep = -enemyStep
            if enemyNormX[norm] >= leftNormBarrier[norm]:
                enemyStep = -enemyStep
            if enemyNormRect[norm].colliderect(playerRect1) and enemyNormVis[norm] != False and immortalityCounter >= 45:
                heartCounter.pop(heartNumber)
                heartCounter.append(False)
                heartNumber = heartNumber - 1
                immortalityCounter = 0            
            for arrow in range(len(arrowX)):
                if arrowRect[arrow].colliderect(enemyNormRect[norm]) and arrowSpeed[arrow] == ARROWSTEP and drawArrow == True and enemyNormVis[norm] != False:
                    enemyNormVis[norm] = False
                    removeArrow(arrow)
                    removeRope()
                    enemyDeathCounter = enemyDeathCounter + 1  
    #Flying               
        for fly in range(numberOfFly):
            enemyFlyY[fly] = enemyFlyY[fly] - enemyStep
            if enemyFlyY[fly] <= highBarrierFly[fly]:
                enemyStep = -enemyStep
            elif enemyFlyY[fly] >= lowBarrierFly[fly]:
                enemyStep = -enemyStep
            if enemyFlyRect[fly].colliderect(playerRect1) and enemyFlyVis[fly] != False and immortalityCounter >= 45:
                heartCounter.pop(heartNumber)
                heartCounter.append(False)
                heartNumber = heartNumber - 1
                immortalityCounter = 0
            for arrow in range(len(arrowX)):
                if arrowRect[arrow].colliderect(enemyFlyRect[fly]) and arrowSpeed[arrow] == ARROWSTEP and arrowVis[arrow] == True and drawArrow == True and enemyFlyVis[fly] != False:
                    enemyFlyVis[fly] = False
                    removeArrow(arrow)
                    removeRope()
                    enemyDeathCounter = enemyDeathCounter + 1
        
    if enemyDeathCounter == numberOfEnemies and stageCounter == 3:
        doorCounter = 2
    elif enemyDeathCounter == numberOfEnemies:
        doorCounter = 1

    if doorRect.colliderect(playerRect1) and enemyDeathCounter == numberOfEnemies:
        nextStage = False
                
                   

            
pygame.quit()







