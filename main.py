import pygame
import sys
import time
import random

from pygame import mixer

#Window/Screen Setup
pygame.init()
pygame.display.set_caption("Scary? Game")
icon = pygame.image.load('entities/iconP.png')
pygame.display.set_icon(icon)
frameSX=1280
frameSY=720
screen=pygame.display.set_mode((frameSX,frameSY))

#level1 test background
background1=pygame.image.load('entities/startmenuTwo2 (1).png')

#Player
playerPic = pygame.image.load("entities/playerImg.png").convert()
size=(20,20) #image size
playerPic=pygame.transform.scale(playerPic, size)
offset = [0, 0]

black = pygame.Color(0, 0, 0)
red = pygame.Color(255, 0, 0)




def main_menu():
    #Game Loop
    while True:
        # Background
        screen.fill((0,0,0))
        #test background
        screen.blit(background1,(0,0))

        #SEES if the color is good / GAMEOVER Moment
        pixel = screen.get_at(pygame.mouse.get_pos())
        if pixel==(0,0,0,255):
            levelOne()



        #Mouse Movement Control with image
        pygame.mouse.set_visible(False)
        mx, my = pygame.mouse.get_pos()
        loc = [mx, my]
        screen.blit(pygame.transform.rotate(playerPic, 0), (loc[0] + offset[0], loc[1] + offset[1]))

        #Exit motive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Update displays
        pygame.display.update()

def levelOne():
    while True:
        #update screen
        l1 = pygame.image.load('entities/levelOne.png')
        screen.fill((0, 0, 0))
        screen.blit(l1, (0, 0))

        # Fail/New level determine
        pixel = screen.get_at(pygame.mouse.get_pos())
        if pixel == black:
            main_menu()
        elif pixel == red:
            level_two()


        pygame.mouse.set_visible(False)
        mx, my = pygame.mouse.get_pos()
        loc = [mx, my]
        screen.blit(pygame.transform.rotate(playerPic, 0), (loc[0] + offset[0], loc[1] + offset[1]))

        #Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Update displays
        pygame.display.update()


def level_two():
    while True:
        #update screen
        l2 = pygame.image.load('entities/level2.png')
        screen.fill((0, 0, 0))
        screen.blit(l2, (0, 0))

        #Fail/New level determine
        pixel = screen.get_at(pygame.mouse.get_pos())
        if pixel == black:
            main_menu()
        elif pixel == red:
            level_three()
        #mouse movement
        pygame.mouse.set_visible(False)
        mx, my = pygame.mouse.get_pos()
        loc = [mx, my]
        screen.blit(pygame.transform.rotate(playerPic, 0), (loc[0] + offset[0], loc[1] + offset[1]))

        #Exit motive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Update displays
        pygame.display.update()

def level_three():
    while True:
        #updates screen
        l3 = pygame.image.load('entities/level3.png')
        screen.fill((0, 0, 0))
        screen.blit(l3, (0, 0))

        #Fail/New level determine
        pixel = screen.get_at(pygame.mouse.get_pos())
        if pixel == black:
            main_menu()
        elif pixel == red:
            finale()
        #mouse movement
        pygame.mouse.set_visible(False)
        mx, my = pygame.mouse.get_pos()
        loc = [mx, my]
        screen.blit(pygame.transform.rotate(playerPic, 0), (loc[0] + offset[0], loc[1] + offset[1]))

        #Exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Update displays
        pygame.display.update()

def finale():
    visuals = ["entities/dwayne.jpg", "entities/tacobell.jpg", "entities/spong.jpg"]
    sounds = ['entities/boom.wav', 'entities/taco.wav', 'entities/ye.wav']
    max = len(visuals) - 1
    picked = random.randint(0, (max))
    print("Thanks for playing :)")
    finpic = pygame.image.load(visuals[picked]).convert()
    size = (1280, 720)  # image size
    finpic = pygame.transform.scale(finpic, size)
    mixer.music.load(sounds[picked])
    mixer.music.play()


    screen.fill(black)
    screen.blit(finpic, (0, 0))
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()

#starts game
main_menu()