import time
import pygame
import os
import random
import sys

HEIGHT = 600
WIDTH = 600

current_volume = 0.05
flag = True
flag1 = True
menu_proc = True
opt_proc = True
game_proc = True

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks")

main_folder = os.path.dirname(__file__)
image_folder = os.path.join(main_folder, "image")
sound_folder = os.path.join(main_folder, "sound")

beton_img = pygame.image.load(os.path.join(image_folder, 'beton.png'))
play_button_img = pygame.image.load(os.path.join(image_folder, 'play_button.png'))
options_button_img = pygame.image.load(os.path.join(image_folder, 'options_button.png'))
quit_button_img = pygame.image.load(os.path.join(image_folder, 'quit_button.png'))
fon1_img = pygame.image.load(os.path.join(image_folder, 'fon1.png'))
player_img = pygame.image.load(os.path.join(image_folder, 'ggu.png'))
volume_button_img = pygame.image.load(os.path.join(image_folder, 'volume_button.png'))
plus_button_img = pygame.image.load(os.path.join(image_folder, 'plus_button.png'))
minus_button_img = pygame.image.load(os.path.join(image_folder, 'minus_button.png'))
back_button_img = pygame.image.load(os.path.join(image_folder, 'back_button.png'))
left_button_img = pygame.image.load(os.path.join(image_folder, 'left_button.png'))
right_button_img = pygame.image.load(os.path.join(image_folder, 'right_button.png'))
fire_button_img = pygame.image.load(os.path.join(image_folder, 'fire_button.png'))
wasd_button_img = pygame.image.load(os.path.join(image_folder, 'wasd_button.png'))
arrows_button_img = pygame.image.load(os.path.join(image_folder, 'arrows_button.png'))
vrag1_img = pygame.image.load(os.path.join(image_folder, 'vrag1.png'))
missile_img = pygame.image.load(os.path.join(image_folder, 'missile.png'))
continue_button_img = pygame.image.load(os.path.join(image_folder, 'continue_button.png'))
newgame_button_img = pygame.image.load(os.path.join(image_folder, 'newgame_button.png'))
menu_button_img = pygame.image.load(os.path.join(image_folder, 'menu_button.png'))
