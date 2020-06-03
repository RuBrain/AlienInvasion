import sys
import pygame
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 51200)
pygame.mixer.init()
pygame.init()

screen = pygame.display.set_mode((1000, 1000))

pygame.display.set_caption("Testing of sound")

while True:

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_q:
                sys.exit()

            elif event.key == pygame.K_SPACE:
                pygame.mixer.music.load('shoot.mp3')
                pygame.mixer.music.play()

    