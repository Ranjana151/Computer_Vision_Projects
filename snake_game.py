import pygame
import random
pygame.init()
pygame.mixer.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)


gameWindow=pygame.display.set_mode((600,400))
pygame.display.set_caption("Hungry Snake")
pygame.display.update()
bgimg=pygame.image.load("snake1.jpg")
bgimg=pygame.transform.scale(bgimg,(600,400))
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,44)
def text_on_screen(text,color,x,y):
    screen=font.render(text,True,color)
    gameWindow.blit(screen,[x,y])

def plot_snake(gameWindow, color, snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])


def gameloop():
    exit_game = False
    game_over = False
    snake_x = 70
    snake_y = 60
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    fps = 20
    score = 0
    snk_length = 1
    snk_list = []
    food_x = random.randint(0, 400)
    food_y = random.randint(100, 380)
    with open("highscore.txt","r")as f:
        highscore=f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt","w")as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_on_screen("Game over!Press enter to continue",black,70,150)
            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        pygame.mixer.music.load("Digital_Voyage.mp3")
                        pygame.mixer.music.play()

                        if event.key == pygame.K_RETURN:
                            pygame.mixer.stop()
                        gameloop()
        else:

            for event in pygame.event.get():
                #print(event)
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        velocity_x=-10
                        velocity_y=0

                    if event.key==pygame.K_RIGHT:
                        velocity_x=10
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-10
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=10
                        velocity_x=0
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y
            if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
                score+=5

                #text_on_screen("Score:"+str(score*5),red,60,60)
                food_x = random.randint(40, 280)
                food_y = random.randint(40, 280)
                snk_length+=3

                if score>int(highscore):
                    highscore=score

            bgimg2 = pygame.image.load("snake4.jpg")
            bgimg2 = pygame.transform.scale(bgimg2, (600, 400))

            gameWindow.fill(white)
            gameWindow.blit(bgimg2,(0,0))
            text_on_screen("Score:" + str(score)+" Highscore: "+str(highscore), white, 170, 10)

            pygame.draw.rect(gameWindow,red,(food_x,food_y,snake_size,snake_size))
            head =[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            if snake_x<0 or snake_x>600 or snake_y<0 or snake_y>400:
                game_over=True




            if head in snk_list[:-1]:
                game_over=True


            plot_snake(gameWindow, black, snk_list,snake_size)

        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
gameloop()
