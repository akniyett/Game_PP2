import pygame
import random
#pylint: disable=no-member
pygame.init()
pygame.font.init()

pygame.display.set_caption("Стреляй или Умирай")

screen = pygame.display.set_mode((800, 600))
x=800
y=600

done = False

backgroundImage = pygame.image.load("galaga.jpg")
playerImage = pygame.image.load("player.png")
player_x = 400
player_y = 500

enemyImage = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(20, 50)

pulyaImage = pygame.image.load("pulya.png")
pulya_x = 420
pulya_y = 470

lifeImage = pygame.image.load("life.png")
life_x=20
life_y=10

num=3


enemy_dx = 5
enemy_dy = 30

pulya_dx = 0
pulya_dy = 5

a=0
cnt=0



def player(x, y):
    screen.blit(playerImage, (x, y))

def enemy(x, y):
    screen.blit(enemyImage, (x, y))


def pulya(x, y):
    screen.blit(pulyaImage, (x, y))

def life(x, y):
    screen.blit(lifeImage, (x, y))

def lifely(x, y):
    screen.blit(lifeNum, (x, y))

def scoret(x, y):
    screen.blit(score, (x, y))

def points(x, y):
    screen.blit(cntd, (x, y))




while not done:
    for event in pygame.event.get():
        # event on quit
        if event.type == pygame.QUIT: # event.type == pygame.KEYDOWN
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]: player_x -= 3
    if pressed[pygame.K_RIGHT]: player_x += 3
        
    screen.fill((0, 0, 0))

    enemy_x += enemy_dx
    if enemy_x < 0 or enemy_x > 736:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy
    pulya_x=player_x+20
    #bullet launch
    if pulya_x==player_x+20 and pulya_y==470:
        lastplayer_x=player_x
    if pressed[pygame.K_SPACE]: 
        pulya_x=lastplayer_x+20
        a=pulya_y
        
    if a>0:
        pulya_x=lastplayer_x+20
        pulya_y -= pulya_dy


    #bullet relaunch
    if pulya_y==0:
        pulya_dy=0
        pulya_x=player_x+20
        pulya_y=470
        num-=1
    if pressed[pygame.K_SPACE]:
        pulya_dy=5
        pulya_x=lastplayer_x+20
        pulya_y-=pulya_dy

    #enemy killing
    if pulya_x >= enemy_x and pulya_x <= enemy_x + 64 and pulya_y <= enemy_y + 64:
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(20, 50)
        pulya_dy=0
        pulya_x=player_x+20
        pulya_y=470
        cnt += 100

    font = pygame.font.SysFont("arial", 25)
    score = font.render("YOUR SCORE: ", True, (185, 60, 223))
    score_x = 600
    score_y = 10

    cntd = font.render(str(cnt), True, (204, 225, 147))
    cntd_x = 750
    cntd_y = 10

    over = pygame.font.SysFont("arial", 50)

    bg = pygame.font.SysFont("arial", 35)
    if num==3:
        lifeNum = bg.render("3", True, (230, 95, 245))
    if num==2:
        lifeNum = bg.render("2", True, (230, 95, 245))
    if num==1:
        lifeNum = bg.render("1", True, (230, 95, 245))
    if num==0 or enemy_y==player_y:
        lifeNum = bg.render("0", True, (230, 95, 245))
        end = over.render("Game Over", True, (230, 95, 245))
        screen.blit(end, (400, 300))
        enemy_dx=0
        enemy_dy=0
        enemy_x=250
        enemy_y=500
        pulya_dy=0
        pulya_x=420
        pulya_y=470
        player_x=400
        player_y=500


    lifeNum_x = 55
    lifeNum_y = 5
    lifeNumRect = lifeNum.get_rect()


    screen.blit(backgroundImage, (0, 0))
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    pulya(pulya_x, pulya_y)
    life(life_x, life_y)
    lifely(lifeNum_x, lifeNum_y)
    scoret(score_x, score_y)
    points(cntd_x, cntd_y)
    pygame.display.flip()