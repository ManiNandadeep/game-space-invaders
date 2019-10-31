import pygame
import random
import math
pygame.init()
screen=pygame.display.set_mode((800,600))
#background
background=pygame.image.load("background.png")
#title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("ufo.png")
pygame.display.set_icon(icon)
#player
playerimg=pygame.image.load("rocket.png")
playerx=370
playery=480
playerxchange=0
#enemy
enemyimg=[]
enemyx=[]
enemyy=[]
enemyxchange=[]
enemyychange=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('alien.png'))
    enemyx.append(random.randint(0,735))
    enemyy.append(random.randint(50,150))
    enemyxchange.append(4)
    enemyychange.append(32)
#bullet
bulletimg=pygame.image.load("bullet.png")
bulletx=0
bullety=480
bulletxchange=0
bulletychange=20
bullet_state="ready"

score_value=0
font = pygame.font.Font('freesansbold.ttf',32)
textx=10
texty=10
def player(x,y):
    screen.blit(playerimg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))
def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt(pow(enemyx-bulletx,2)+pow(enemyy-bullety,2))
    if distance <27:
        return True
    else:
        return False
def show_score(x,y):
    score=font.render('score:'+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def game_over():
    text=font.render('GAME OVER',True,(255,255,255))
    screen.blit(text,(250,250))
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            playerxchange=-5
        if event.key==pygame.K_RIGHT:
            playerxchange=+5
        if event.key==pygame.K_SPACE:
            if bullet_state is"ready":
               bulletx=playerx
               fire_bullet(bulletx,playery)

    if event.type==pygame.KEYUP:
        if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
            playerxchange=0

    playerx+=playerxchange
    if playerx<=0:
        playerx=0
    if playerx>=736:
        playerx=736

    for i in range(num_of_enemies):
        #game over
        if enemyy[i]>420:
            for j in range(num_of_enemies):
                enemyy[j]=2000
            game_over()
        enemyx[i]+=enemyxchange[i]
        if enemyx[i]<=0:
            enemyxchange[i]=4
            enemyy[i]+=enemyychange[i]
        if enemyx[i]>=736:
            enemyxchange[i]=-4
            enemyy[i]+=enemyychange[i]
        collision=iscollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision is True:
            bullet=480
            bullet_state="ready"
            score_value+=1
            enemyx[i]=random.randint(0,735)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)

    
    if bullety<=0:
        bullety=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety-=bulletychange

    show_score(textx,texty)
    player(playerx,playery)
    pygame.display.update()

