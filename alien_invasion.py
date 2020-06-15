import pygame
from pygame.sprite import Group
import sys
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame import mixer

pygame.mixer.pre_init(44100, -16, 2, 51200)
pygame.mixer.init()

def run_game():
    # Инициализирует игру и создает объект экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)

    pygame.display.set_caption("Alien Invasion")

    # Создание корабля, группы пуль и группы пришельцев.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Создание флота пришельцев.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play()

    # Запуск основного цикла игры
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, aliens, ship)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()